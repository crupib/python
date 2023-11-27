import argparse
parser = argparse.ArgumentParser()
parser.add_argument("sub", choices=['Physics', 'Maths', 'Biology'])
args=parser.parse_args()
print ("My subject is ", args.sub)
