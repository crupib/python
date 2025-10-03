import random
def guessing_game():
    answer = random.randint(0,100)
    while True:
        user_guess = int(input("Guess a number between 0 and 100: "))
        if user_guess == answer:
            print("You guessed right!")
            break
        if user_guess > answer:
            print("Too high!")
        else:
            print("Too low!")
guessing_game()
