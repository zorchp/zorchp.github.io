---
tags: brpc
categories: brpc
---

## 写在前面

## bthread 的原理







## benchmark

```cpp
#include <bits/stdc++.h>
#include <bthread.h>
// #define use_bthread
using namespace std;
using namespace std::chrono;

class TimeCost {
public:
    TimeCost() : _start_time(std::chrono::high_resolution_clock::now()) {}

    void begin_time_point() { _start_time = std::chrono::high_resolution_clock::now(); }

    double get_time_cost(bool is_reset = false) {
        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration =
            std::chrono::duration_cast<std::chrono::microseconds>(end_time - _start_time);
        double cost = static_cast<double>(duration.count()) / 1e3;

        if (is_reset) {
            _start_time = std::chrono::high_resolution_clock::now();
        }

        return cost;
    }

private:
    std::chrono::high_resolution_clock::time_point _start_time;
};

template <typename MutexType>
class Mutex {
    MutexType _mutex;

public:
    Mutex() {
        if constexpr (std::is_same_v<MutexType, pthread_mutex_t>) {
            pthread_mutex_init(&_mutex, nullptr);
        } else {
            bthread_mutex_init(&_mutex, nullptr);
        }
    }

    ~Mutex() {
        if constexpr (std::is_same_v<MutexType, pthread_mutex_t>) {
            pthread_mutex_destroy(&_mutex);
        } else {
            bthread_mutex_destroy(&_mutex);
        }
    }

    void lock() {
        if constexpr (std::is_same_v<MutexType, pthread_mutex_t>) {
            pthread_mutex_lock(&_mutex);
        } else {
            bthread_mutex_lock(&_mutex);
        }
    }

    void unlock() {
        if constexpr (std::is_same_v<MutexType, pthread_mutex_t>) {
            pthread_mutex_unlock(&_mutex);
        } else {
            bthread_mutex_unlock(&_mutex);
        }
    }
};
struct BthreadTag {};
struct PthreadTag {};


template <typename ThreadTag>
struct ThreadTraits;

template <>
struct ThreadTraits<BthreadTag> {
    using thread_t = bthread_t;
    using mutex_t  = bthread_mutex_t;

    static int create(thread_t* t, void* (*fn)(void*), void* arg) {
        return bthread_start_background(t, nullptr, fn, arg);
    }
    static int join(thread_t t) {
        return bthread_join(t, nullptr);
    }
};

template <>
struct ThreadTraits<PthreadTag> {
    using thread_t = pthread_t;
    using mutex_t  = pthread_mutex_t;

    static int create(thread_t* t, void* (*fn)(void*), void* arg) {
        return pthread_create(t, nullptr, fn, arg);
    }
    static int join(thread_t t) {
        return pthread_join(t, nullptr);
    }
};

```



```cpp
#include "utils.h"

constexpr static int N = 10;

template <typename Tag>
void t1_impl(int thr_num) {
    using Traits = ThreadTraits<Tag>;
    using thread_t = typename Traits::thread_t;
    using mutex_t = typename Traits::mutex_t;

    Mutex<mutex_t> mutex;
    std::vector<thread_t> tids(thr_num);

    vector<int> line(N);

    struct Arg {
        int* line_p = nullptr;
        Mutex<mutex_t>* p_mutex = nullptr;
        int idx = 0;
        int ret = -1;
    };

    auto task_fn = [](void* arg) -> void* {
        auto arg_inner = static_cast<Arg*>(arg);
        arg_inner->p_mutex->lock();
        arg_inner->line_p[arg_inner->idx % N] += 1;
        arg_inner->p_mutex->unlock();

        arg_inner->ret = 0;
        return nullptr;
    };

    vector<unique_ptr<Arg>> ctx_v;
    ctx_v.reserve(thr_num);
    TimeCost tc;
    for (int i{}; i < thr_num; ++i) {
        auto ctx = make_unique<Arg>();
        ctx->line_p = line.data();
        ctx->idx = i;
        ctx->p_mutex = &mutex;

        Traits::create(&tids[i], task_fn, ctx.get());
        ctx_v.push_back(std::move(ctx));
    }
    for (auto tid : tids) {
        Traits::join(tid);
    }
    cout << "time cost:" << tc.get_time_cost() << "ms\n";
    for (auto& ctx : ctx_v) {
        if (ctx->ret != 0) {
            printf("err\n");
        } else {
        }
    }
    int p = 0;
    for (auto x : line) {
        printf("line[%d]=%d\n", p++, x);
    }
}

int main(int argc, char** argv) {
    if (argc != 3) {
        fprintf(stderr, "Usage : %s thread_type(0:bthread,1:pthread) thr_num\n", argv[0]);
        return 1;
    }
    int type = atoi(argv[1]);
    int n = atoi(argv[2]);

    if (type == 0) {
        printf("using bthread\n");
        t1_impl<BthreadTag>(n);
    } else {
        printf("using pthread\n");
        t1_impl<PthreadTag>(n);
    }
    return 0;
}
```

