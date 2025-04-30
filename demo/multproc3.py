import multiprocessing

# Function to put data into the queue
def put_data(q):
    for item in range(5):
        q.put(item)
    q.put(None)  # Use a sentinel to indicate the end of data

# Function to get and process data from the queue
def process_data(q):
    while True:
        item = q.get()
        print("item = ", item)
        if item is None:
            break  # Exit when the sentinel is encountered
        print(f"Processed: {item}")

if __name__ == "__main__":
    # Create a multiprocessing queue
    my_queue = multiprocessing.Queue()

    # Create two processes to put and process data
    put_process = multiprocessing.Process(target=put_data, args=(my_queue,))
    process_process = multiprocessing.Process(target=process_data, args=(my_queue,))

    # Start the processes
    put_process.start()
    process_process.start()

    # Wait for both processes to finish
    put_process.join()
    process_process.join()

    print("Both processes have finished.")
