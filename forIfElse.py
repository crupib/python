def contains_even_number(l):
   for elt in l:
      if elt %2 == 0:
        print("list contains an even number")
   else:
        print("list does not contain an even number")

mylist = [1,4,6,9,10]
contains_even_number(mylist)
