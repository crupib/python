class Game:
    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("\nMinimum Number of Questions = 1")
            print("Hence, number of questions will be set to 1")
        elif value > 10:
            self._noOfQuestions = 10
            print("\nMaximum Number of Questions = 10")
            print("Hence, number of questions will be set to 10")
        else:
            self._noOfQuestions = value
            
class BinaryGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0

        for i in range(self.noOfQuestions):
            base10 = randint(1, 100)
            userResult = input("\nPlease convert %d to binary: " %(base10))
            while True:
                try:
                    answer = int(userResult, base = 2)
                    if answer == base10:
                        print("Correct Answer!")
                        score = score + 1
                        break
                    else:
                        print("Wrong answer. The correct answer is {:b}.".format(base10))
                        break
                except:
                    print("You did not enter a binary number. Please try again.")
                    userResult = input("\nPlease convert %d to binary: " %(base10))
            
        return score                    

class MathGame(Game):
    def generateQuestions(self):
        from random import randint
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ['', '', '', '']
        operatorDict = {1:' + ', 2:' - ', 3:'*', 4:'**'}

        for i in range(self.noOfQuestions):
            for index in range(0, 5):
                numberList[index] = randint(1, 9)
            #refer to explanation below
            for index in range(0, 4):
                if index > 0 and symbolList[index - 1] == '**':
                    symbolList[index] = operatorDict[randint(1, 3)]
                else:
                    symbolList[index] = operatorDict[randint(1, 4)]

            questionString = str(numberList[0])

            for index in range(0, 4):
                questionString = questionString + symbolList[index] + str(numberList[index+1])

            result = eval(questionString)

            questionString = questionString.replace("**", "^")

            userResult = input("\nPlease evaluate %s: "%(questionString))

            while True:
                try:
                    answer = int(userResult)
                    if answer == result:
                        print("Correct Answer!")
                        score = score + 1
                        break
                    else:
                        print("Wrong answer. The correct answer is {:d}.".format(result))
                        break
                except:
                    print("You did not enter a valid number. Please try again.")
                    userResult = input("\nPlease evaluate %s: "%(questionString))
            
        return score            
                    
'''
Explanation

Starting from the second item (i.e. index = 1) in symbolList, the line if index > 0 and symbolList[index-1] == '**': checks if the previous item in symbolList is the ** symbol..
 
If it is, the statement symbolList[index] = operatorDict[randint(1, 3)] will execute. In this case, the range given to the randint function is from 1 to 3. Hence, the ** symbol, which has a key of 4 in operatorDict  will NOT be  assigned to symbolList[index].

On the other hand, if it is not, the statement symbolList[index] = operatorDict[randint(1, 4)] will execute. Since the range given to the randint function is 1 to 4, the numbers 1, 2, 3 or 4 will be generated. Hence, the symbols +, -, * or ** will be assigned to symbolList[index].

'''
                                            
        

            
        
