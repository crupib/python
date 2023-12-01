def checkIfPrime(numberToCheck):
	for x in range(2,numberToCheck):
		if (numberToCheck%x == 0):
			return False
	return True
def main():
  answer = checkIfPrime(13)
  print(answer)
if __name__ == '__main__':
   main()

