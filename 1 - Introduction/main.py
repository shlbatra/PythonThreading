import threading 
import time 
#main thread
#Make a thread -> use function here 
'''
def func():
    print('ran')
    time.sleep(1) #thread hang switch to other thread
    print('done')

#Thread object defined below     
#Second thread
x = threading.Thread(target=func, args=()) #making a thread, pass arguments to function ex. (4,) - tuple 

x.start()  #this starts the second thread
print(threading.activeCount())
'''
print("\n\n")

def func1():
    print('ran')
    time.sleep(1) #thread hang switch to other thread
    print('done')
    time.sleep(1)
    print('now done')

#Thread object defined below     
#Second thread
x = threading.Thread(target=func1, args=()) #making a thread, pass arguments to function ex. (4,) - tuple 
x.start()  #this starts the second thread
print(threading.activeCount())
time.sleep(1.2)
print('finally')