from tqdm import tqdm
import time
bar = tqdm(range(10))
tot = 0
for i in bar:
  time.sleep(2)
  tot += i
  bar.set_postfix({"total":tot})
