class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words 
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'
class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'
class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'
class BabbleingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'
def who_says(obj):
    print(obj.who(), 'says', obj.says())
hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())
brook = BabbleingBrook()
print(brook.who())
print(brook.says())
print("**************************************")
who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)
