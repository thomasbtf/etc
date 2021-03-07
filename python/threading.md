Source: https://www.python-engineer.com/courses/advancedpython/15-thread-vs-process/

# Threads
A thread is an entity within a process that can be scheduled for execution (also known as "leightweight process"). A process can spawn multiple threads. The main difference to processes is that all threads within a process share the same memory.

Positive key facts: 
- Multiple threads can be spawned within one process 
- Memory is shared between all threads 
- Starting a thread is faster than starting a process 
- Great for I/O-bound tasks 
- Leightweight 
- low memory footprint

Negative key facts: 
- One GIL for all threads, i.e. threads are limited by GIL 
- Multithreading has no effect for CPU-bound tasks due to the GIL 
- Not interruptible/killable -> be careful with memory leaks 
- increased potential for race conditions

## Threading in Python
Use the `threading` module.

Despite the GIL it is useful for I/O-bound tasks when your program has to talk to slow devices, like a hard drive or a network connection. With threading the program can use the time waiting for these devices and intelligently do other tasks in the meantime.

Example: Download website information from multiple sites. Use a thread for each site.