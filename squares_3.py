#Maths Puzzles - www.101computing.net/maths-puzzles/
# What 2 square numbers subtract to make 31?
acc=[] 
newacc=[] 
pairs=[]
#We will only test poisitve numbers up to 1,000!
for i in range(0,1000):
  if i**2 < 125:
     acc.append(i)
print(acc)
for i in acc:
    for j in acc:
       if (i)**2 + (j)**2 + (j+1)**2 == 125:
          newacc.append(i)
          newacc.append(j)
          newacc.append(j+1)
print(newacc)
print(acc)
print(pairs)
