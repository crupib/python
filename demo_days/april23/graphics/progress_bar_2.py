from tqdm import tqdm
import time
bar = tqdm(range(10), desc="Example bar")
for i in bar:
  time.sleep(2)
