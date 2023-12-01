word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
letter_counts2 = {letter: word.count(letter) for letter in set(word)}
print(letter_counts2)
