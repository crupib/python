pip3 install memory-profiler
mprof run mem_profile_script.py 
Multithreading in Python: Multithreading is the process of executing multiple threads
 (tasks) concurrently within a single process. 
Multiprocessing in Python: Multiprocessing is the process of executing
 multiple processes concurrently within a system. 

Differences between Multithreading and Multiprocessing:

1. Memory Sharing: Multithreading shares the same memory space, 
   while multiprocessing uses separate memory space.
2. Speed: Multithreading is faster as compared to multiprocessing
   since there is no overhead of creating a new process.
3. CPU Utilization: Multiprocessing utilizes more CPU resources 
   as compared to multithreading because of the overhead of creating a new process.
4. Memory Efficiency: Multithreading is memory-efficient as it shares the same 
   memory space, while multiprocessing requires more memory space.
5. Security: Multiprocessing provides better security as compared to multithreading because each
   process has its own internal security and because it can help to isolate different parts 
   of your code from each other.
mprof run -M multproc.py 
mprof plot
