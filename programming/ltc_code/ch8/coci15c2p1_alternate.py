# Idea motivated by Alisha D'souza


DIGIT_TO_LETTERS = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
                    6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}


n = int(input())

words = []

for i in range(n):
    words.append(input())

target = input()

total = 0

for word in words:
    if len(word) == len(target):
        good = True
        for i in range(len(target)):
            if not word[i] in DIGIT_TO_LETTERS[int(target[i])]:
                good = False
        if good:
            total = total + 1

print(total)
