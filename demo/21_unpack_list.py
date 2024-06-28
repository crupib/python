names = [ 'John', 'Mary', 'Lisa', 'Rose']
names2 = [ 'Rose' ,'Mary', 'Lisa', 'John']
boy, *girls = names

print(boy)
print(girls)

*girls, boy = names2
print(boy)
print(girls)
