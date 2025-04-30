import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
string_answer = int(answer)
if number1 + number2 == string_answer:
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))
