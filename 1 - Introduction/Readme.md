- Concurrency, Threading and Parallelism
- Processor has multiple cores (2,4,8,16,32,etc) in CPU
- Amt of cores in processor means amt of things that can happen at the same time
-  4 cores -> 4 operations at the same time (low level computation) - parallelism
- Clock speed (2.6Ghz) - each core runs at 2.6 million opns per sec
- Thread -> One set of operation needs to happen and assigned to core, core have operations run on. 
- Threading -> Determine when to run diff things (threads) on the same CPU core, changing order in which we do specific operations on the same core
- Thread hangs for time ex.I/O wait , not executing then another thread can continue on the same core -> Concurrent programming (Doing things in diff timing sequences)
- Ex. 
Prog1 -> 
print(1)
time.sleep(10)
print(2)

Thread for Prog1

Distribute to two threads (Prog2)
t1 
print(1)
time.sleep(10)
print(3)

t2
print(2)

t1 runs then t2 runs till t1 is hanging and then t1 finishes. 
O/P 1, 2, 3 

Used in games app -> Server related commands run in thread for i/O while your game is running - display graphics, 

Multi processed -> Run threads on muliple CPU cores at the same time. 

- Thread Sycronization with dot joint method to complete a specific thread and not let other threads run when the specific thread is in hang state 

- generally it is hard to figure out which thread is running when in a multithreading env. 

- Way to create a thread in Python
    - x = threading.Thread(target=<function name>, args=(pass it as tuple with min 1 comma))