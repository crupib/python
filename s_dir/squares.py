#Maths Puzzles - www.101computing.net/maths-puzzles/

# What 2 square numbers subtract to make 31?

#We will only test poisitve numbers up to 1,000!
for i in range(0,1000):
  for j in range(0,i):
    if (i**2 - j**2) == 31:
       print(i)
       print(j)
       print(str(i) + "**2 - " + str(j) + "**2 = " + str(i**2) + " - " + str(j**2) + " == 31")
