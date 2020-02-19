from threading import Thread, Condition
import time
import random

condition = Condition()
n = 0 
class ProducerThread(Thread):
    def run(self):
        global n
        while True:
            condition.acquire()
            n+=1
            condition.notify()
            condition.release()
            time.sleep(random.random())

class ConsumerThread(Thread):
    def run(self):
        while True:
            condition.acquire()
            condition.wait()
            print("n = ", n)
            condition.notify()
            condition.release()
            time.sleep(random.random())

ProducerThread().start()
ConsumerThread().start()

