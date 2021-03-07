Source: https://www.python-engineer.com/courses/advancedpython/15-thread-vs-process/

# Processes
A Process is an instance of a program, e.g. a Python interpreter. They are independent from each other and do not share the same memory.

Positive key facts: 
- A new process is started independently from the first process 
- Takes advantage of multiple CPUs and cores 
- Separate memory space 
- Memory is not shared between processes 
- One GIL (Global interpreter lock) for each process, i.e. avoids GIL limitation 
- Great for CPU-bound processing 
- Child processes are interruptable/killable

Negative key facts: 
- Starting a process is slower that starting a thread
- Larger memory footprint
- IPC (inter-process communication) is more complicated

## Multiprocessing
Use the `multiprocessing` module.

It is useful for CPU-bound tasks that have to do a lot of CPU operations for a large amount of data and require a lot of computation time. With multiprocessing you can split the data into equal parts an do parallel computing on different CPUs.

Example: Calculate the square numbers for all numbers from 1 to 1000000. Divide the numbers into equal sized parts and use a process for each subset.