ifile=open("data/t2mG_00", "r")
lines=ifile.readlines()
data=[tuple(line.strip().split()) for line in lines]
print(data[0])
