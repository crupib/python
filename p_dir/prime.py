def coprime(a,b):
   for i in range(2, min(a,b) + 1):
     if a % i == 0 and b % i == 0:
        return False
   return True
print( coprime(4,9))
print (not(coprime(4, 12)))
