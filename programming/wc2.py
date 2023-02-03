def word_count(str):
    words = str.split()
    counts = len(words)
    return counts

line = input()
print( word_count(line))
