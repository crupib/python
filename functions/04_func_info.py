def myfunction(a, b):
    c = 5
    return a + b

print(myfunction.__code__.co_argcount)      # 2
print(myfunction.__code__.co_name)          # myfunction
print(myfunction.__code__.co_varnames)      # ('a', 'b')
print(myfunction.__code__.co_firstlineno)   # 1
