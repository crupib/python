import math
import time
#tic = time.perf_counter()
tic = time.time()
for x in range(1,1000000):
	x*math.pi/x
#toc = time.perf_counter()
toc = time.time()
print(tic)
print(toc)
print(toc - tic)
