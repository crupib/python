"""
Solving producer-consumer problem using semaphores
"""
import threading

N = 0
consumed = threading.Semaphore(0)
produced = threading.Semaphore(1)

def produce():
    global N
    N+=1
    return 0

def producer():
    front = 0
    global N
    while True:
        consumed.acquire()
        produced.release()
        if N > 10 :
           exit(0)
        produce()

def consume():
    global N
    print("n= ", N)

def consumer():
    while True:
        produced.acquire()
        consumed.release()
        if N > 10 :
           exit(0)
        consume()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
