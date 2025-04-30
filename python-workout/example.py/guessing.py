import random
def guessing_game():
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input("Guess a number between 0 and 100: "))
        if user_guess == answer:
            print(f'you guessed right!')
            break
        if user_guess < answer:
            print(f'Too low!')
        else:
            print(f'Too high!')
guessing_game()