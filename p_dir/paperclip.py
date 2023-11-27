import pyperclip

copy = input("Enter the text you want to copy to clipboard ")
pyperclip.copy(copy)
text = pyperclip.paste()
print(text)                                                                                   
