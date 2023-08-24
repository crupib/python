from pipe import select, where, chain, traverse, groupby, dedup
arr = [1,2,3,4,5]
print(list(map(lambda x: x*2, filter(lambda x: x % 2 == 0, arr))))
arr = [1,2,3,4,5,6,7,8]
print(list(arr
 | where(lambda x: x % 2 == 0)
 | select(lambda x:x*2)))
arr = [1,2,3,4,5]
print(list(arr | where(lambda x: x%2 == 0)))
print(list(arr | select(lambda x: x*2)))
nested = [[1,2,[3]],[4,5]]
print(list(nested|chain))
print(list(nested|traverse))
fruits = [
	{"name" : "apple", "price": [2,5]},
	{"name" : "orange", "price": 4},
	{"name" : "grape", "price": 5},
	{"name" : "kumquat", "price": 7}
]
print(list(fruits 
             | select(lambda fruit: fruit["price"])
             | traverse))
print(list(
          (1,2,3,4,5,6,7,8,9)
          | groupby(lambda x: "Even" if x % 2 == 0 else "Odd")
          | select(lambda x: {x[0]: list(x[1])})
      ))
print(list(
          (1,2,3,4,5,6,7,8,9)
          | groupby(lambda x: "Even" if x % 2 == 0 else "Odd")
          | select(lambda x: {x[0]: list(x[1] | where(lambda x: x>2))})
      ))
arr = [1,1,2,2,3,4,5,6,6,7,9,3,3,1]
print(list(arr|dedup))
print(list(arr | dedup(lambda key: key < 5)))
data = [
   {"name": "apple", "count": 2},
   {"name": "orange", "count": 4},
   {"name": "grape", "count": None},
   {"name": "orange", "count": 7}
]
print(list(data
           | dedup(key=lambda fruit: fruit["name"])
           | select(lambda fruit: fruit["count"])
           | where(lambda count: isinstance(count,int)))
)
