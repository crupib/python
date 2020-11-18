import argparse
parser=argparse.ArgumentParser(description="add numbers")
parser.add_argument("first", type=int)
parser.add_argument("second", type=int)
args = parser.parse_args()
x = args.first
y = args.second
z = x+y
print ('addition of {} and {} = {}'.format(x,y,z))
