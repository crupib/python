# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):
	if num >= 1:
		DecimalToBinary(num // 2)
	print(num % 2, end = '')

# Driver Code
if __name__ == '__main__':
   dec_val = 1024
   DecimalToBinary(dec_val)
   print("\n")
