def calc (int1,oper,int2):
	if oper == '.' :
   		return int1*int2
	elif oper == '+' :
   		return int1+int2
	elif oper == '-' :
   		return int1-int2
	elif oper == '/' :
   		return int1/int2
	else:
   		print("invalid operator\n")

int1 = input("Input first integer : ")
int2 = input("Input second integer : ")
oper = input("Input operator : ")

print(calc(int(int1),oper,int(int2)))
