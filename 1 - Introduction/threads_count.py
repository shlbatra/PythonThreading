import threading 
import time 
'''
def count(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.01)
        
for _ in range(2):
    x = threading.Thread(target=count, args=(10,))
    x.start()
    
print("Done")
'''

'''
#hard to figure out which thread is running when in a multithreading env. 
def count1(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.01)
        
def count2(n):
    for i in range(1,n+1):
        print(i)
        time.sleep(0.02)
        
x = threading.Thread(target=count1, args=(10,))
x.start()

y = threading.Thread(target=count2, args=(10,))
y.start()
    
print("Done")
'''

#Using global variables with threads 

ls = []  #global variable / memory 

def count1(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)
        
def count2(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)
        
x = threading.Thread(target=count1, args=(5,))
x.start()
x.join()
y = threading.Thread(target=count2, args=(5,))
y.start()
y.join()

# O/P -> [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]. run first x thread and then y thread
#time.sleep(0.5)  -> Alt where we can keep increasing time here 

#Thread Sycronization with dot joint method to get complete array after both threads complete
#x.join() #Do not move past this variable till this thread finishes, keep executing both threads till they complete 
#y.join()
#Get O/p -> [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

print(ls) # Simply get (1,1) and not full list -> When both threads sleep get main thread where we print 