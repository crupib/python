# Python program to check
# if a word is isogram or not
def is_isogram(word):

# Convert the word or sentence in lower case letters.
 clean_word = word.lower()
# Make an empty list to append unique letters
 letter_list = []
 for letter in clean_word:
# If letter is an alphabet then only check
  if letter.isalpha():
     if letter in letter_list:
        return False
     letter_list.append(letter)
  else:
     if letter != "-" and letter != " ":
        return False
 return True

if __name__ == '__main__':
# print(is_isogram("Machine"))       
# print(is_isogram("isogram"))      
# print(is_isogram("GeeksforGeeks"))     
# print(is_isogram("Alphabet"))           
 print(is_isogram("lumberjacks"))           
 print(is_isogram("background"))           
 print(is_isogram("downstream"))           
 print(is_isogram("six-year-old"))           
 print(is_isogram("six year old"))           
 print(is_isogram("six/year/old"))           
