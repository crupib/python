import multiprocessing

def square(x):
    return x ** 2

if __name__ == '__main__':
    numbers = list(range(1,50))
#    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    with multiprocessing.Pool() as pool:
        result = pool.map(square, numbers)
    
    print(result)
