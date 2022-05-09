def get_xos_count(xxoos_list):
   ocount = 0
   xcount = 0
   for item in xxoos_list:
      if item == "O":
        ocount += 1
      if item == "X":
        xcount += 1
   return [ocount, xcount]
def test_xos (xcount,ocount):
   if xcount == 0 and ocount == 0:
      return True
   if xcount == ocount :
     return True
   return False

xxoos_none = ["a","B","S","H", "I", "T"] 
xxoos_odd = ["O","X","X","O","O"]
xxoos_even = ["O","X","X","O"]
ocounts, xcounts  = get_xos_count(xxoos_even)
print(test_xos(ocounts,xcounts))
ocounts, xcounts = get_xos_count(xxoos_odd)
print(test_xos(ocounts,xcounts))
ocounts, xcounts = get_xos_count(xxoos_none)
print(test_xos(ocounts,xcounts))
