import sys
if '/Users/williamcrupi/Documents/github/project_python/mymods' not in sys.path:
   sys.path.append('/Users/williamcrupi/Documents/github/project_python/mymods')
import prime
def main():
  answer = prime.checkIfPrime(13)
  print(answer)
if __name__ == '__main__':
   main()


