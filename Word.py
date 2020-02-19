class Word():
	def __init__(self, text):
		self.text = text
	def __eq__(self,word2):
		return self.text.lower() == word2.text.lower()
	def __add__(self,word2):
		return self.text + word2.text
	def __(self,word2):
		return self.text + word2.text

def main():
	first = Word('ha')
	second = Word('HA')
	third  = Word('eh')
	print(first == second)
	print(second == third)
	print(first+second)
if __name__ == "__main__":
	main()
