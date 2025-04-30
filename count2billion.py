import time

def count_to_one_billion():
    start_time = time.time()  # Start the timer
    count = 0
    for i in range(1, 1_000_000_001):
        count += 1
    end_time = time.time()  # Stop the timer
    elapsed_time = end_time - start_time
    print(f"Time taken to count to one billion: {elapsed_time:.2f} seconds")

# Run the program
count_to_one_billion()

