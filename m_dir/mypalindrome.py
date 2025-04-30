def palindrome(word):
    lowercase = word.lower()
    alpha_only = ''.join([i for i in lowercase if i.isalpha()])
    return alpha_only == alpha_only[::-1]
print(palindrome('A nut, for a jar of tuna!'))
