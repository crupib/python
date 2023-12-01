from collections import Counter

my_list = ['a', 'b', 'b', 'a', 'a', 'a', 'c', 'c', 'b', 'd']
print(Counter(my_list).most_common()[1][0])
