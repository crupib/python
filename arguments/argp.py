import argparse
parser = argparse.ArgumentParser(description="sample argument parser")
parser.add_argument("user", nargs='?',default="Admin")
args=parser.parse_args()
print(args.user)
if args.user=="Admin":
   print ("Hello Admin")
else:
   print ("Hello Guest")
