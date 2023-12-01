import time

start_time = time.time()

for loop in range(1, 100000000): 
    pass

print('FINISHED EXECUTION')
print("--- %s seconds ---" % round(time.time() - start_time, 4))
