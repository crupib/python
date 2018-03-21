class Game:
    def __init__(self, noOfQuestions=0):
        print('This is GameClass')
        if noOfQuestions > 0:
            if noOfQuestions > 10:
                print("Maximum Number of Questions = 10")
                print("Hence, number of questions will be set to 10")
                self._noOfQuestions = 10
            else:
                self._noOfQuestions = noOfQuestions
        else:
            print("Minimum Number of Questions = 1")
            print("Hence, number of questions will be set to 1")
            self._noOfQuestions = 1
#        print(self._noOfQuestions)

    @property
    def noOfQuestions(self):
        print("noOfQuestions prop")
        return self._noOfQuestions

    @noOfQuestions.getter
    def noOfQuestions(self):
        print("In Getter")
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        print("In Setter")
        if value > 0:
            if value > 10:
                print("Maximum Number of Questions = 10")
                print("Hence, number of questions will be set to 10")
                self._noOfQuestions = 10
            else:
                self._noOfQuestions = value
        else:
            print("Minimum Number of Questions = 1")
            print("Hence, number of questions will be set to 1")
            self._noOfQuestions = 1
print("instruc a = Game(20)")
a = Game(1000)
print("instruc print(a.noOfQuestions)")
print(a.noOfQuestions)
print("instruc print(a.noOfQuestions = 15)")
a.noOfQuestions = -99  
print("instruc print(a.noOfQuestions)")
print(a.noOfQuestions)
