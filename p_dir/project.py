from gametasks import printInstructions, getUserScore, updateUserScore
from gameclasses import Game, MathGame, BinaryGame

try:
    mathInstructions = '''
In this game, you will be given a simple arithmetic question.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.
'''

    binaryInstructions = '''
In this game, you will be given a number in base 10.
Your task is to convert this number to base 2.
Each correct answer gives you one mark.
No mark is deducted for wrong answers.
'''
    mg = MathGame()
    bg = BinaryGame()

    userName = input("\nPlease enter your username: ")

    score = int(getUserScore(userName))

    if score == -1:
        newUser = True
        score = 0
    else:
        newUser = False

    print("\nHello %s, welcome to the game." %(userName))
    print("Your current score is %d." %(score))

    userChoice = 0

    while userChoice != '-1':
        game = input("\nMath Game (1) or Binary Game (2)?: ")
        while game != '1' and game != '2':
            print("You did not enter a valid choice. Please try again.")
            game = input("\nMath Game (1) or Binary Game (2)?: ")

        numPrompt = input("\nHow many questions do you want per game (1 to 10)?: ")
        while True:
            try:
                num = int(numPrompt)
                break
            except:
                print("You did not enter a valid number. Please try again.")
                numPrompt = input("\nHow many questions do you want per game (1 to 10)?: ")

            
        if game == '1':
            mg.noOfQuestions = num
            printInstructions(mathInstructions)
            score = score + mg.generateQuestions()
        else:
            bg.noOfQuestions = num
            printInstructions(binaryInstructions)
            score = score + bg.generateQuestions()

        print("\nYour current score is %d." %(score))

        userChoice = input("\nPress Enter to continue or -1 to end: ")

    updateUserScore(newUser, userName, str(score))

except Exception as e:
    print("An unknown error occurred. Program will exit.")
    print("Error: ", e)


    
