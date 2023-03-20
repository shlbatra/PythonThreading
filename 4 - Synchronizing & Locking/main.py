import threading 
import time

class myThread1(threading.Thread): #class inherit from threading class
    '''
    Create diff class for diff thread types you want to define
    '''
    def __init__(self,threadId,name,count):#thread count down from count
        threading.Thread.__init__(self) #call parent contructor method or threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name 
        self.count=count
        
    def run(self): #define what thread would do  -> run a function
        '''
        finish first thread and then get into the next thread here
        '''
        print(f"Starting: {self.name} \n")
        threadLock.acquire() #lock thread and not run any thread til this finishes
        print_time(self.name,1,self.count)
        threadLock.release() #once thread finishes, release the lock for other threads to run
        
        print(f"Exiting: {self.name} \n")
        

class myThread2(threading.Thread): #class inherit from threading class
    '''
    Create diff class for diff thread types you want to define
    '''
    def __init__(self,threadId,name,count):#thread count down from count
        threading.Thread.__init__(self) #call parent contructor method or threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name 
        self.count=count
        
    def run(self): #define what thread would do  -> run a function
        '''
        finish first thread and then get into the next thread here
        '''
        print(f"Starting: {self.name} \n")
        threadLock.acquire() #Check if any other thread is locking 
        threadLock.release() #once check validated no other thread locking then immediate release the lock 
        print_time(self.name,1,self.count)
        print(f"Exiting: {self.name} \n")


def print_time(name,delay,count):
    while count:
        time.sleep(delay)
        print(f"{name}, {time.ctime(time.time())}, {count} \n")
        count-=1
        
threadLock=threading.Lock() #object to lock threads
#Create new threads 
thread1=myThread1(1,"Payment",5)  #id, name, count
thread2=myThread2(2,"Sending Email",10)
thread3=myThread2(2,"Loading Page",3)

#simulate the same situation as explained in Readme payment example. 
thread1.start() #run thread
thread2.start() 
thread3.start()
thread1.join() #thread exit without completing, wait for thread to finish before terminating the main program thread
thread2.join()
thread3.join()

print("Done main thread")