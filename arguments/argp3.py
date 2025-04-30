import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("-s","--surname")
args = parser.parse_args()
print ("My name is ", args.name, end=' ')
if args.surname:
   print (args.surname)
else:
   print("\n")
