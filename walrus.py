fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}

def make_lemonade(count):
    print("1 lemonade coming up")

def out_of_stock():
    print("Go fuck your self")

#count = fresh_fruit.get('lemon',0)
#print(count)
if count := fresh_fruit.get('lemon',0):
   make_lemonade(count)
else:
   out_of_stock()
