from datetime import datetime
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
start_time = datetime.now()
print(fibonacci(40))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
