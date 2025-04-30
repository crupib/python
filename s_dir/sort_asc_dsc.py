number_list = [3, 29, 4, 11, -4, 6, 1, 8, 5, 33]
def sort_list(passlist, ascdesc):
      if ascdesc == 'asc': 
         passlist.sort()
      elif ascdesc == "desc": 
         passlist.sort(reverse=True)
print(number_list)
sort_list(number_list,"none")
print(number_list)
