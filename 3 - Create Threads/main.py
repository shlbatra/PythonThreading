import threading 
import time

class myThread(threading.Thread): #class inherit from threading class
    '''
    Create diff class for diff thread types you want to define
    '''
    def __init__(self,threadId,name,count):#thread count down from count
        threading.Thread.__init__(self) #call parent contructor method or threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name 
        self.count=count
        
    def run(self): #define what thread would do  -> run a function
        print(f"Starting: {self.name} \n")
        print_time(self.name,1,self.count)
        print(f"Exiting: {self.name} \n")
        
def print_time(name,delay,count):
    while count:
        time.sleep(delay)
        print(f"{name}, {time.ctime(time.time())}, {count} \n")
        count-=1
        
#Create new threads 
thread1=myThread(1,"Thread-1",10)  #id, name, count
thread2=myThread(2,"Thread-2",5)

thread1.start() #run thread
thread2.start() 
thread1.join() #thread exit without completing, wait for thread to finish before terminating the main program thread
thread2.join()

print("Done main thread")