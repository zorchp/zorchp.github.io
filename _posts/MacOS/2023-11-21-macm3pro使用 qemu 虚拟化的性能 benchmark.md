---

---





相差无几, (感觉系统也会有影响, 下次试试都在 Ubuntu 下跑)



### Ubuntu-x86_64-2c4g

```bash
 ==> sysbench cpu --cpu-max-prime=20000000 --threads=2 run
sysbench 1.0.20 (using system LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 2
Initializing random number generator from current time


Prime numbers limit: 20000000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:     0.05

General statistics:
    total time:                          43.1130s
    total number of events:              2

Latency (ms):
         min:                                43111.53
         avg:                                43112.18
         max:                                43112.83
         95th percentile:                    42899.63
         sum:                                86224.35

Threads fairness:
    events (avg/stddev):           1.0000/0.00
    execution time (avg/stddev):   43.1122/0.00

```





### Qemu-archlinux-3c2g

```bash
[arch@archlinux ~]$ sysbench cpu --cpu-max-prime=20000000 --threads=2 run
sysbench 1.0.20 (using system LuaJIT 2.0.5)

Running the test with following options:
Number of threads: 2
Initializing random number generator from current time


Prime numbers limit: 20000000

Initializing worker threads...

Threads started!

CPU speed:
    events per second:     0.05

General statistics:
    total time:                          38.0986s
    total number of events:              2

Latency (ms):
         min:                                38065.45
         avg:                                38080.95
         max:                                38096.46
         95th percentile:                    37819.22
         sum:                                76161.91

Threads fairness:
    events (avg/stddev):           1.0000/0.00
    execution time (avg/stddev):   38.0810/0.02
```

