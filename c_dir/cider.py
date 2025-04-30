fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}

def make_lemonade(count):
    print("1 lemonade coming up")

def make_cider(count):
    print("1 ass smelling cider")

def out_of_stock():
    print("Go fuck your self")

if (count := fresh_fruit.get('apple',0)) >= 4:
   make_cider(count)
else:
   out_of_stock()
