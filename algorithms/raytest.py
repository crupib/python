import ray
import time
ray.init()

@ray.remote
def f(x):
    return x * x
time.sleep(10)
futures = [f.remote(i) for i in range(4)]
print(ray.get(futures))
