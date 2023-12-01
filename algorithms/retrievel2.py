#!/usr/bin/env python3
import requests
import time
import threading
from queue import Queue
urls = [one_line.strip()
        for one_line in open('urls.txt')]
length = {}
queue = Queue()
start_time = time.time()
threads = [ ]
def get_length(one_url):
    response = requests.get(one_url)
    queue.put((one_url, len(response.content)))
# Launch our function in a thread
print("Launching")
for one_url in urls:
    t = threading.Thread(target=get_length, args=(one_url,))
    threads.append(t)
    t.start()
# Joining all
print("Joining")
for one_thread in threads:
    one_thread.join()
# Retrieving + printing
print("Retrieving + printing")
while not queue.empty():
    one_url, length = queue.get()
    print("{0:30}: {1:8,}".format(one_url, length))
end_time = time.time()
total_time = end_time - start_time
print("\nTotal time: {0:.3} seconds".format(total_time))
