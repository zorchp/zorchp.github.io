---

---

## 源码

>   来自 llvm16.0.4 最新版, 目录:
>
>   ```cpp
>   /opt/homebrew/Cellar/llvm/16.0.4/include/c++/v1/__algorithm/sort.h
>   ```

推荐一个在线源码网站: [sort.h source code [ClickHouse/contrib/llvm-project/libcxx/include/__algorithm/sort.h] - Woboq Code Browser](https://clickhouse.com/codebrowser/ClickHouse/contrib/llvm-project/libcxx/include/__algorithm/sort.h.html#284);

## 主要逻辑

### 主函数

```cpp
template <class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI _LIBCPP_CONSTEXPR_SINCE_CXX20
void sort(_RandomAccessIterator __first, _RandomAccessIterator __last) {
  std::sort(__first, __last, __less<typename iterator_traits<_RandomAccessIterator>::value_type>());
}
```

默认采用递增序(`less<>`)

然后是重载的三参数版本:

```cpp
template <class _RandomAccessIterator, class _Comp>
inline _LIBCPP_HIDE_FROM_ABI _LIBCPP_CONSTEXPR_SINCE_CXX20
void sort(_RandomAccessIterator __first, _RandomAccessIterator __last, _Comp __comp) {
  std::__sort_impl<_ClassicAlgPolicy>(std::move(__first), std::move(__last), __comp);
}
```

`std::__sort_impl`这个函数就是排序的核心. 

```cpp
template <class _AlgPolicy, class _RandomAccessIterator, class _Comp>
inline _LIBCPP_HIDE_FROM_ABI _LIBCPP_CONSTEXPR_SINCE_CXX20
void __sort_impl(_RandomAccessIterator __first, _RandomAccessIterator __last, _Comp& __comp) {
  std::__debug_randomize_range<_AlgPolicy>(__first, __last);

  using _Comp_ref = __comp_ref_type<_Comp>;
  if (__libcpp_is_constant_evaluated()) {
    std::__partial_sort<_AlgPolicy>(__first, __last, __last, __comp);

  } else {
    using _WrappedComp = typename _WrapAlgPolicy<_AlgPolicy, _Comp_ref>::type;
    _Comp_ref __comp_ref(__comp);
    _WrappedComp __wrapped_comp(__comp_ref);
    std::__sort<_WrappedComp>(std::__unwrap_iter(__first), std::__unwrap_iter(__last), __wrapped_comp);
  }
}
```

忽略 Debug 相关的函数, 主要看逻辑部分, 首先判断是否为常量表达式: 

>   [Other Builtins (Using the GNU Compiler Collection (GCC))](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html#index-_005f_005fbuiltin_005fis_005fconstant_005fevaluated);

```cpp
Built-in Function: bool __builtin_is_constant_evaluated (void)
The __builtin_is_constant_evaluated function is available only in C++. The built-in is intended to be used by implementations of the std::is_constant_evaluated C++ function. Programs should make use of the latter function rather than invoking the built-in directly.

The main use case of the built-in is to determine whether a constexpr function is being called in a constexpr context. A call to the function evaluates to a core constant expression with the value true if and only if it occurs within the evaluation of an expression or conversion that is manifestly constant-evaluated as defined in the C++ standard. Manifestly constant-evaluated contexts include constant-expressions, the conditions of constexpr if statements, constraint-expressions, and initializers of variables usable in constant expressions. For more details refer to the latest revision of the C++ standard.
```

>   不是很理解这个...

这部分采用堆排序:(`__partial_sort_impl`)

```cpp
template <class _AlgPolicy, class _Compare, class _RandomAccessIterator, class _Sentinel>
_LIBCPP_HIDE_FROM_ABI _LIBCPP_CONSTEXPR_SINCE_CXX20
_RandomAccessIterator __partial_sort_impl(
    _RandomAccessIterator __first, _RandomAccessIterator __middle, _Sentinel __last, _Compare&& __comp) {
  if (__first == __middle) {
    return _IterOps<_AlgPolicy>::next(__middle, __last);
  }

  std::__make_heap<_AlgPolicy>(__first, __middle, __comp);

  typename iterator_traits<_RandomAccessIterator>::difference_type __len = __middle - __first;
  _RandomAccessIterator __i = __middle;
  for (; __i != __last; ++__i)
  {
      if (__comp(*__i, *__first))
      {
          _IterOps<_AlgPolicy>::iter_swap(__i, __first);
          std::__sift_down<_AlgPolicy>(__first, __comp, __len, __first);
      }
  }
  std::__sort_heap<_AlgPolicy>(std::move(__first), std::move(__middle), __comp);

  return __i;
}
```

另一部分是**主要逻辑**:(`std::__sort`)

```cpp
template <class _WrappedComp, class _RandomAccessIterator>
_LIBCPP_HIDDEN void __sort(_RandomAccessIterator __first, _RandomAccessIterator __last, _WrappedComp __wrapped_comp) {
  typedef typename iterator_traits<_RandomAccessIterator>::difference_type difference_type;
  difference_type __depth_limit = 2 * std::__log2i(__last - __first);

  using _Unwrap = _UnwrapAlgPolicy<_WrappedComp>;
  using _AlgPolicy = typename _Unwrap::_AlgPolicy;
  using _Compare = typename _Unwrap::_Comp;
  _Compare __comp = _Unwrap::__get_comp(__wrapped_comp);
  std::__introsort<_AlgPolicy, _Compare>(__first, __last, __comp, __depth_limit);
}
```

调用了一个名为`__introsort`的函数, 其实就是**内省排序**了. (使用堆排序和插入排序解决快排在长度较短时出现的递归调用过多的问题) 

>   `__log2i`函数是用来计算最高位索引的:(其实就是 G++常用的`__lg`)
>
>   ```cpp
>   template <typename _Number>
>   inline _LIBCPP_HIDE_FROM_ABI _Number __log2i(_Number __n) {
>    if (__n == 0)
>      return 0;
>    if (sizeof(__n) <= sizeof(unsigned))
>      return sizeof(unsigned) * CHAR_BIT - 1 - __libcpp_clz(static_cast<unsigned>(__n));
>    if (sizeof(__n) <= sizeof(unsigned long))
>      return sizeof(unsigned long) * CHAR_BIT - 1 - __libcpp_clz(static_cast<unsigned long>(__n));
>    if (sizeof(__n) <= sizeof(unsigned long long))
>      return sizeof(unsigned long long) * CHAR_BIT - 1 - __libcpp_clz(static_cast<unsigned long long>(__n));
>   
>    _Number __log2 = 0;
>    while (__n > 1) {
>      __log2++;
>      __n >>= 1;
>    }
>    return __log2;
>   }
>   ```
>
>   里面的 clz 相关函数是用来计算前导零的(count leader zero)
>
>   CHAR_BIT宏值为 8(一字节的位数)
>
>   最后计算出来的这个值:
>
>   ```c
>   __depth_limit = 2 * std::__log2i(__last - __first);
>   ```
>
>   就是递归最大深度限制



```cpp
template <class _AlgPolicy, class _Compare, class _RandomAccessIterator>
void __introsort(_RandomAccessIterator __first, _RandomAccessIterator __last, _Compare __comp,
                 typename iterator_traits<_RandomAccessIterator>::difference_type __depth) {
  using _Ops = _IterOps<_AlgPolicy>;

  typedef typename iterator_traits<_RandomAccessIterator>::difference_type difference_type;
  typedef typename iterator_traits<_RandomAccessIterator>::value_type value_type;
  const difference_type __limit =
      is_trivially_copy_constructible<value_type>::value && is_trivially_copy_assignable<value_type>::value ? 30 : 6;
  while (true) {
  __restart: // 配合后面的 goto 语句(这里竟然用了goto!)
    difference_type __len = __last - __first;
    switch (__len) {
    case 0:
    case 1:
      return; // 长度为 0, 1 直接跳出
    case 2: // 比较后交换
      if (__comp(*--__last, *__first))
        _IterOps<_AlgPolicy>::iter_swap(__first, __last);
      return;
    case 3:
      std::__sort3_maybe_branchless<_AlgPolicy, _Compare>(__first, __first + difference_type(1), --__last, __comp);
      return;
    case 4:
      std::__sort4_maybe_branchless<_AlgPolicy, _Compare>(
          __first, __first + difference_type(1), __first + difference_type(2), --__last, __comp);
      return;
    case 5:
      std::__sort5_maybe_branchless<_AlgPolicy, _Compare>(
          __first, __first + difference_type(1), __first + difference_type(2), __first + difference_type(3),
          --__last, __comp);
      return;
    }
    if (__len <= __limit) {
      std::__insertion_sort_3<_AlgPolicy, _Compare>(__first, __last, __comp);
      return;
    }
    // __len > 5
    if (__depth == 0) {
      // Fallback to heap sort as Introsort suggests.
      std::__partial_sort<_AlgPolicy, _Compare>(__first, __last, __last, __comp); // 快排
      return;
    }
    --__depth;// 递归一次, 降低深度
    _RandomAccessIterator __m = __first;
    _RandomAccessIterator __lm1 = __last;
    --__lm1;
    unsigned __n_swaps;
    {//找中位数, median
      difference_type __delta;
      if (__len >= 1000) {
        __delta = __len / 2;
        __m += __delta;
        __delta /= 2;
        __n_swaps = std::__sort5_wrap_policy<_AlgPolicy, _Compare>(
            __first, __first + __delta, __m, __m + __delta, __lm1, __comp);
      } else {
        __delta = __len / 2;
        __m += __delta;
        __n_swaps = std::__sort3<_AlgPolicy, _Compare>(__first, __m, __lm1, __comp);
      }
    }
    // *__m is median
    // partition [__first, __m) < *__m and *__m <= [__m, __last)
    // (this inhibits tossing elements equivalent to __m around unnecessarily)
    _RandomAccessIterator __i = __first;
    _RandomAccessIterator __j = __lm1;
    // j points beyond range to be tested, *__m is known to be <= *__lm1
    // The search going up is known to be guarded but the search coming down isn't.
    // Prime the downward search with a guard.
    if (!__comp(*__i, *__m)) // if *__first == *__m
    {
      // *__first == *__m, *__first doesn't go in first part
      // manually guard downward moving __j against __i
      while (true) {
        if (__i == --__j) {
          // *__first == *__m, *__m <= all other elements
          // Parition instead into [__first, __i) == *__first and *__first < [__i, __last)
          ++__i; // __first + 1
          __j = __last;
          if (!__comp(*__first, *--__j)) // we need a guard if *__first == *(__last-1)
          {
            while (true) {
              if (__i == __j)
                return; // [__first, __last) all equivalent elements
              if (__comp(*__first, *__i)) {
                _Ops::iter_swap(__i, __j);
                ++__n_swaps;
                ++__i;
                break;
              }
              ++__i;
            }
          }
          // [__first, __i) == *__first and *__first < [__j, __last) and __j == __last - 1
          if (__i == __j)
            return;
          while (true) {
            while (!__comp(*__first, *__i))
              ++__i;
            while (__comp(*__first, *--__j))
              ;
            if (__i >= __j)
              break;
            _Ops::iter_swap(__i, __j);
            ++__n_swaps;
            ++__i;
          }
          // [__first, __i) == *__first and *__first < [__i, __last)
          // The first part is sorted, sort the second part
          // std::__sort<_Compare>(__i, __last, __comp);
          __first = __i;
          goto __restart;
        }
        if (__comp(*__j, *__m)) {
          _Ops::iter_swap(__i, __j);
          ++__n_swaps;
          break; // found guard for downward moving __j, now use unguarded partition
        }
      }
    }
    // It is known that *__i < *__m
    ++__i;
    // j points beyond range to be tested, *__m is known to be <= *__lm1
    // if not yet partitioned...
    if (__i < __j) {
      // known that *(__i - 1) < *__m
      // known that __i <= __m
      while (true) {
        // __m still guards upward moving __i
        while (__comp(*__i, *__m))
          ++__i;
        // It is now known that a guard exists for downward moving __j
        while (!__comp(*--__j, *__m))
          ;
        if (__i > __j)
          break;
        _Ops::iter_swap(__i, __j);
        ++__n_swaps;
        // It is known that __m != __j
        // If __m just moved, follow it
        if (__m == __i)
          __m = __j;
        ++__i;
      }
    }
    // [__first, __i) < *__m and *__m <= [__i, __last)
    if (__i != __m && __comp(*__m, *__i)) {
      _Ops::iter_swap(__i, __m);
      ++__n_swaps;
    }
    // [__first, __i) < *__i and *__i <= [__i+1, __last)
    // If we were given a perfect partition, see if insertion sort is quick...
    if (__n_swaps == 0) {
      using _WrappedComp = typename _WrapAlgPolicy<_AlgPolicy, _Compare>::type;
      _WrappedComp __wrapped_comp(__comp);
      bool __fs = std::__insertion_sort_incomplete<_WrappedComp>(__first, __i, __wrapped_comp);
      if (std::__insertion_sort_incomplete<_WrappedComp>(__i + difference_type(1), __last, __wrapped_comp)) {
        if (__fs)
          return;
        __last = __i;
        continue;
      } else {
        if (__fs) {
          __first = ++__i;
          continue;
        }
      }
    }
    // sort smaller range with recursive call and larger with tail recursion elimination
    if (__i - __first < __last - __i) { // 这里执行快排: 递归
      std::__introsort<_AlgPolicy, _Compare>(__first, __i, __comp, __depth);
      __first = ++__i;
    } else {
      std::__introsort<_AlgPolicy, _Compare>(__i + difference_type(1), __last, __comp, __depth);
      __last = __i;
    }
  }
}
```



下面根据 Switch 的不同判断来分析:

### case 3:

```cpp
template <class, class _Compare, class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI __enable_if_t<__use_branchless_sort<_Compare, _RandomAccessIterator>::value, void>
__sort3_maybe_branchless(_RandomAccessIterator __x1, _RandomAccessIterator __x2, _RandomAccessIterator __x3,
                         _Compare __c) {
  std::__cond_swap<_Compare>(__x2, __x3, __c);
  std::__partially_sorted_swap<_Compare>(__x1, __x2, __x3, __c);
}
```

这里用到了`__sort3_maybe_branchless`这个函数, 先将 x2 和 x3 排好序, 然后和 x1 排序. 

`__cond_swap`函数: 条件满足则交换, 用在了两数比较之中. 很好理解, 本质就是判断符号然后执行交换(最基本的交换, 并没有玩出花样)

```cpp
// Ensures that __c(*__x, *__y) is true by swapping *__x and *__y if necessary.
template <class _Compare, class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI void __cond_swap(_RandomAccessIterator __x, _RandomAccessIterator __y, _Compare __c) {
  // Note: this function behaves correctly even with proxy iterators (because it relies on `value_type`).
  using value_type = typename iterator_traits<_RandomAccessIterator>::value_type;
  bool __r = __c(*__x, *__y);
  value_type __tmp = __r ? *__x : *__y;
  *__y = __r ? *__y : *__x;
  *__x = __tmp;
}
```

`__partially_sorted_swap`函数, 先将两个数交换, 然后放入此函数中与第一参数(x1)比较并排序. 

```cpp
// Ensures that *__x, *__y and *__z are ordered according to the comparator __c,
// under the assumption that *__y and *__z are already ordered.
template <class _Compare, class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI void __partially_sorted_swap(_RandomAccessIterator __x, _RandomAccessIterator __y,
                                                          _RandomAccessIterator __z, _Compare __c) {
  // Note: this function behaves correctly even with proxy iterators (because it relies on `value_type`).
  using value_type = typename iterator_traits<_RandomAccessIterator>::value_type;
  bool __r = __c(*__z, *__x);
  value_type __tmp = __r ? *__z : *__x;
  *__z = __r ? *__x : *__z;
  __r = __c(__tmp, *__y);
  *__x = __r ? *__x : *__y;
  *__y = __r ? *__y : __tmp;
}
```

这里再介绍一个函数(仅为前向迭代器设计), 叫做`__sort3`, 后面会用:

```cpp
template <class _AlgPolicy, class _Compare, class _ForwardIterator>
_LIBCPP_HIDE_FROM_ABI
_LIBCPP_CONSTEXPR_SINCE_CXX14 unsigned __sort3(_ForwardIterator __x, _ForwardIterator __y, _ForwardIterator __z,
                                               _Compare __c) {
  using _Ops = _IterOps<_AlgPolicy>;

  unsigned __r = 0;
  if (!__c(*__y, *__x))   // if x <= y
  {
    if (!__c(*__z, *__y)) // if y <= z
      return __r;         // x <= y && y <= z
                          // x <= y && y > z
    _Ops::iter_swap(__y, __z);     // x <= z && y < z
    __r = 1;
    if (__c(*__y, *__x))  // if x > y
    {
      _Ops::iter_swap(__x, __y);   // x < y && y <= z
      __r = 2;
    }
    return __r;           // x <= y && y < z
  }
  if (__c(*__z, *__y))    // x > y, if y > z
  {
    _Ops::iter_swap(__x, __z);     // x < y && y < z
    __r = 1;
    return __r;
  }
  _Ops::iter_swap(__x, __y);       // x > y && y <= z
  __r = 1;                // x < y && x <= z
  if (__c(*__z, *__y))    // if y > z
  {
    _Ops::iter_swap(__y, __z);     // x <= y && y < z
    __r = 2;
  }
  return __r;
}                         // x <= y && y <= z
```





### case 4:

```cpp
template <class, class _Compare, class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI __enable_if_t<__use_branchless_sort<_Compare, _RandomAccessIterator>::value, void>
__sort4_maybe_branchless(_RandomAccessIterator __x1, _RandomAccessIterator __x2, _RandomAccessIterator __x3,
                         _RandomAccessIterator __x4, _Compare __c) {
  std::__cond_swap<_Compare>(__x1, __x3, __c);
  std::__cond_swap<_Compare>(__x2, __x4, __c);
  std::__cond_swap<_Compare>(__x1, __x2, __c);
  std::__cond_swap<_Compare>(__x3, __x4, __c);
  std::__cond_swap<_Compare>(__x2, __x3, __c);
}

template <class _AlgPolicy, class _Compare, class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI __enable_if_t<!__use_branchless_sort<_Compare, _RandomAccessIterator>::value, void>
__sort4_maybe_branchless(_RandomAccessIterator __x1, _RandomAccessIterator __x2, _RandomAccessIterator __x3,
                         _RandomAccessIterator __x4, _Compare __c) {
  std::__sort4<_AlgPolicy, _Compare>(__x1, __x2, __x3, __x4, __c);
}
```

直接用前面的两数排序, 有点归并的味道了, 先排序x1和 x3, 然后 x2 和 x4, 以此类推. 

### case 5:

```cpp
template <class, class _Compare, class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI __enable_if_t<__use_branchless_sort<_Compare, _RandomAccessIterator>::value, void>
__sort5_maybe_branchless(_RandomAccessIterator __x1, _RandomAccessIterator __x2, _RandomAccessIterator __x3,
                         _RandomAccessIterator __x4, _RandomAccessIterator __x5, _Compare __c) {
  std::__cond_swap<_Compare>(__x1, __x2, __c);
  std::__cond_swap<_Compare>(__x4, __x5, __c);
  std::__partially_sorted_swap<_Compare>(__x3, __x4, __x5, __c);
  std::__cond_swap<_Compare>(__x2, __x5, __c);
  std::__partially_sorted_swap<_Compare>(__x1, __x3, __x4, __c);
  std::__partially_sorted_swap<_Compare>(__x2, __x3, __x4, __c);
}

template <class _AlgPolicy, class _Compare, class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI __enable_if_t<!__use_branchless_sort<_Compare, _RandomAccessIterator>::value, void>
__sort5_maybe_branchless(_RandomAccessIterator __x1, _RandomAccessIterator __x2, _RandomAccessIterator __x3,
                         _RandomAccessIterator __x4, _RandomAccessIterator __x5, _Compare __c) {
  std::__sort5_wrap_policy<_AlgPolicy, _Compare>(__x1, __x2, __x3, __x4, __x5, __c);
}
```



### 选择排序(未使用)

```cpp
// Assumes size > 0
template <class _AlgPolicy, class _Compare, class _BidirectionalIterator>
_LIBCPP_HIDE_FROM_ABI
_LIBCPP_CONSTEXPR_SINCE_CXX14 void __selection_sort(_BidirectionalIterator __first, _BidirectionalIterator __last,
                                                    _Compare __comp) {
  _BidirectionalIterator __lm1 = __last;
  for (--__lm1; __first != __lm1; ++__first) {
    _BidirectionalIterator __i = std::__min_element<_Compare>(__first, __last, __comp);
    if (__i != __first)
      _IterOps<_AlgPolicy>::iter_swap(__first, __i);
  }
}
```





### 插入排序

```cpp
template <class _AlgPolicy, class _Compare, class _BidirectionalIterator>
_LIBCPP_HIDE_FROM_ABI
void __insertion_sort(_BidirectionalIterator __first, _BidirectionalIterator __last, _Compare __comp) {
  using _Ops = _IterOps<_AlgPolicy>;

  typedef typename iterator_traits<_BidirectionalIterator>::value_type value_type;
  if (__first != __last) {
    _BidirectionalIterator __i = __first;
    for (++__i; __i != __last; ++__i) {
      _BidirectionalIterator __j = __i;
      value_type __t(_Ops::__iter_move(__j));
      for (_BidirectionalIterator __k = __i; __k != __first && __comp(__t, *--__k); --__j)
        *__j = _Ops::__iter_move(__k);
      *__j = std::move(__t);
    }
  }
}

template <class _AlgPolicy, class _Compare, class _RandomAccessIterator>
_LIBCPP_HIDE_FROM_ABI
void __insertion_sort_3(_RandomAccessIterator __first, _RandomAccessIterator __last, _Compare __comp) {
  using _Ops = _IterOps<_AlgPolicy>;

  typedef typename iterator_traits<_RandomAccessIterator>::difference_type difference_type;
  typedef typename iterator_traits<_RandomAccessIterator>::value_type value_type;
  _RandomAccessIterator __j = __first + difference_type(2);
  std::__sort3_maybe_branchless<_AlgPolicy, _Compare>(__first, __first + difference_type(1), __j, __comp);
  for (_RandomAccessIterator __i = __j + difference_type(1); __i != __last; ++__i) {
    if (__comp(*__i, *__j)) {
      value_type __t(_Ops::__iter_move(__i));
      _RandomAccessIterator __k = __j;
      __j = __i;
      do {
        *__j = _Ops::__iter_move(__k);
        __j = __k;
      } while (__j != __first && __comp(__t, *--__k));
      *__j = std::move(__t);
    }
    __j = __i;
  }
}

template <class _WrappedComp, class _RandomAccessIterator>
_LIBCPP_HIDDEN bool __insertion_sort_incomplete(
    _RandomAccessIterator __first, _RandomAccessIterator __last, _WrappedComp __wrapped_comp) {
  using _Unwrap = _UnwrapAlgPolicy<_WrappedComp>;
  using _AlgPolicy = typename _Unwrap::_AlgPolicy;
  using _Ops = _IterOps<_AlgPolicy>;

  using _Compare = typename _Unwrap::_Comp;
  _Compare __comp = _Unwrap::__get_comp(__wrapped_comp);

  typedef typename iterator_traits<_RandomAccessIterator>::difference_type difference_type;
  switch (__last - __first) {
  case 0:
  case 1:
    return true;
  case 2:
    if (__comp(*--__last, *__first))
      _IterOps<_AlgPolicy>::iter_swap(__first, __last);
    return true;
  case 3:
    std::__sort3_maybe_branchless<_AlgPolicy, _Compare>(__first, __first + difference_type(1), --__last, __comp);
    return true;
  case 4:
    std::__sort4_maybe_branchless<_AlgPolicy, _Compare>(
        __first, __first + difference_type(1), __first + difference_type(2), --__last, __comp);
    return true;
  case 5:
    std::__sort5_maybe_branchless<_AlgPolicy, _Compare>(
        __first, __first + difference_type(1), __first + difference_type(2), __first + difference_type(3),
        --__last, __comp);
    return true;
  }
  typedef typename iterator_traits<_RandomAccessIterator>::value_type value_type;
  _RandomAccessIterator __j = __first + difference_type(2);
  std::__sort3_maybe_branchless<_AlgPolicy, _Compare>(__first, __first + difference_type(1), __j, __comp);
  const unsigned __limit = 8;
  unsigned __count = 0;
  for (_RandomAccessIterator __i = __j + difference_type(1); __i != __last; ++__i) {
    if (__comp(*__i, *__j)) {
      value_type __t(_Ops::__iter_move(__i));
      _RandomAccessIterator __k = __j;
      __j = __i;
      do {
        *__j = _Ops::__iter_move(__k);
        __j = __k;
      } while (__j != __first && __comp(__t, *--__k));
      *__j = std::move(__t);
      if (++__count == __limit)
        return ++__i == __last;
    }
    __j = __i;
  }
  return true;
}

template <class _AlgPolicy, class _Compare, class _BidirectionalIterator>
_LIBCPP_HIDE_FROM_ABI
void __insertion_sort_move(_BidirectionalIterator __first1, _BidirectionalIterator __last1,
                           typename iterator_traits<_BidirectionalIterator>::value_type* __first2, _Compare __comp) {
  using _Ops = _IterOps<_AlgPolicy>;

  typedef typename iterator_traits<_BidirectionalIterator>::value_type value_type;
  if (__first1 != __last1) {
    __destruct_n __d(0);
    unique_ptr<value_type, __destruct_n&> __h(__first2, __d);
    value_type* __last2 = __first2;
    ::new ((void*)__last2) value_type(_Ops::__iter_move(__first1));
    __d.template __incr<value_type>();
    for (++__last2; ++__first1 != __last1; ++__last2) {
      value_type* __j2 = __last2;
      value_type* __i2 = __j2;
      if (__comp(*__first1, *--__i2)) {
        ::new ((void*)__j2) value_type(std::move(*__i2));
        __d.template __incr<value_type>();
        for (--__j2; __i2 != __first2 && __comp(*__first1, *--__i2); --__j2)
          *__j2 = std::move(*__i2);
        *__j2 = _Ops::__iter_move(__first1);
      } else {
        ::new ((void*)__j2) value_type(_Ops::__iter_move(__first1));
        __d.template __incr<value_type>();
      }
    }
    __h.release();
  }
}
```



### case 6:(len大于 5)

使用快速排序, `__partial_sort`. 

```cpp
template <class _AlgPolicy, class _Compare, class _RandomAccessIterator, class _Sentinel>
_LIBCPP_HIDE_FROM_ABI _LIBCPP_CONSTEXPR_SINCE_CXX20
_RandomAccessIterator __partial_sort(_RandomAccessIterator __first, _RandomAccessIterator __middle, _Sentinel __last,
                                     _Compare& __comp) {
  if (__first == __middle) // 区间为 0, 直接返回
      return _IterOps<_AlgPolicy>::next(__middle, __last);

  std::__debug_randomize_range<_AlgPolicy>(__first, __last);

  auto __last_iter =
      std::__partial_sort_impl<_AlgPolicy>(__first, __middle, __last, static_cast<__comp_ref_type<_Compare> >(__comp));

  std::__debug_randomize_range<_AlgPolicy>(__middle, __last);

  return __last_iter;
}
```



执行 partition:

```cpp
template <class _AlgPolicy, class _Compare, class _RandomAccessIterator, class _Sentinel>
_LIBCPP_HIDE_FROM_ABI _LIBCPP_CONSTEXPR_SINCE_CXX20
_RandomAccessIterator __partial_sort_impl(
    _RandomAccessIterator __first, _RandomAccessIterator __middle, _Sentinel __last, _Compare&& __comp) {
  if (__first == __middle) {
    return _IterOps<_AlgPolicy>::next(__middle, __last);
  }

  std::__make_heap<_AlgPolicy>(__first, __middle, __comp);

  typename iterator_traits<_RandomAccessIterator>::difference_type __len = __middle - __first;
  _RandomAccessIterator __i = __middle;
  for (; __i != __last; ++__i)
  {
      if (__comp(*__i, *__first))
      {
          _IterOps<_AlgPolicy>::iter_swap(__i, __first);
          std::__sift_down<_AlgPolicy>(__first, __comp, __len, __first);
      }
  }
  std::__sort_heap<_AlgPolicy>(std::move(__first), std::move(__middle), __comp);

  return __i;
}
```

这里用到了堆排序:

```cpp
template <class _AlgPolicy, class _Compare, class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI _LIBCPP_CONSTEXPR_SINCE_CXX14
void __sort_heap(_RandomAccessIterator __first, _RandomAccessIterator __last, _Compare&& __comp) {
  __comp_ref_type<_Compare> __comp_ref = __comp;

  using difference_type = typename iterator_traits<_RandomAccessIterator>::difference_type;
  for (difference_type __n = __last - __first; __n > 1; --__last, (void) --__n)
    std::__pop_heap<_AlgPolicy>(__first, __last, __comp_ref, __n);
}
```

堆排序的核心就是弹出调整(堆化 heapify)

```cpp
template <class _AlgPolicy, class _Compare, class _RandomAccessIterator>
inline _LIBCPP_HIDE_FROM_ABI _LIBCPP_CONSTEXPR_SINCE_CXX14
void __pop_heap(_RandomAccessIterator __first, _RandomAccessIterator __last, _Compare& __comp,
    typename iterator_traits<_RandomAccessIterator>::difference_type __len) {
  _LIBCPP_ASSERT(__len > 0, "The heap given to pop_heap must be non-empty");

  __comp_ref_type<_Compare> __comp_ref = __comp;

  using value_type = typename iterator_traits<_RandomAccessIterator>::value_type;
  if (__len > 1) {
    value_type __top = _IterOps<_AlgPolicy>::__iter_move(__first);  // create a hole at __first
    _RandomAccessIterator __hole = std::__floyd_sift_down<_AlgPolicy>(__first, __comp_ref, __len);
    --__last;

    if (__hole == __last) {
      *__hole = std::move(__top);
    } else {
      *__hole = _IterOps<_AlgPolicy>::__iter_move(__last);
      ++__hole;
      *__last = std::move(__top);
      std::__sift_up<_AlgPolicy>(__first, __hole, __comp_ref, __hole - __first);
    }
  }
}
```

