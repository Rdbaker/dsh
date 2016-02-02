Ryan Baker
rdbaker

Distributed Shell


******************************************
        DEPENDENCIES (Server side)
******************************************
`gcc --version` returns the following:
gcc (GCC) 4.8.3 20140911 (Red Hat 4.8.3-9)


`lscpu` returns the following:
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                1
On-line CPU(s) list:   0
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 63
Model name:            Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
Stepping:              2
CPU MHz:               2400.050
BogoMIPS:              4800.10
Hypervisor vendor:     Xen
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              30720K
NUMA node0 CPU(s):     0


`lsblk` returns the following:
NAME    MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
xvda    202:0    0   8G  0 disk 
└─xvda1 202:1    0   8G  0 part /


`free` returns the following:
             total       used       free     shared    buffers     cached
Mem:        503380     433520      69860         60      22940     331256
-/+ buffers/cache:      79324     424056
Swap:            0          0          0


`uname -a` returns the following:
Linux ip-172-31-58-142 4.1.10-17.31.amzn1.x86_64 #1 SMP Sat Oct 24 01:31:37 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux



******************************************
        Running It (Server side)
******************************************



******************************************
        Running It (Client side)
******************************************
