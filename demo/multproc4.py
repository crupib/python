import multiprocessing

# Function to increment a shared counter safely using a lock
def increment_counter(counter, lock):
    for _ in range(100000):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    # Create a shared counter and a lock to protect it
    counter = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()

    # Create two processes to increment the counter
    process1 = multiprocessing.Process(target=increment_counter, args=(counter, lock))
    process2 = multiprocessing.Process(target=increment_counter, args=(counter, lock))

    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Counter:", counter.value)
