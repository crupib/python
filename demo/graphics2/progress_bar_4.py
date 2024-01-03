from tqdm import tqdm
import time
bar=tqdm(range(10), 
      bar_format="{percentage:3.0f}% |{bar}| {elapsed}/{remaining}"
     )
for i in bar:
  time.sleep(2)
