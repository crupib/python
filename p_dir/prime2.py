def coprime_alternate(a,b):
   is_coprime = True
   for i in range(2, min(a,b) + 1):
     if a % i == 0 and b % i == 0:
        is_coprime = False
        break
     return is_coprime

print( coprime_alternate(4,9))
print (not(coprime_alternate(4, 12)))
