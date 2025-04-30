from tqdm import tqdm
import time
for i in tqdm(range(10)):
    time.sleep(0.1)
items = [1, 2, 3, 4, 5]
for item in tqdm(items, desc="Processing items"):
    # Process each item
    time.sleep(0.2)
