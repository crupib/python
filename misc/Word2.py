class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self,word2):
        return self.text.lower() == word2.text.lower()
    def __add__(self,word2):
        return self.text + word2.text
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("'  + self.text +  '")'

def main():
# nope
    first = Word('ha')
    second = Word('HA')
    third  = Word('eh')
    print(first == second)
    print(second == third)
    print(first+second)
    print(first)
if __name__ == "__main__":
	main()
