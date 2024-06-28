dict = { "one" : 1, "two": 2, "three": 3 }
#with get method
print(dict.get("fourth")) #None
print(dict.get("two")) # 2
lst = [ 1, 2, 3, 4, 5]
print(lst[::2]) #[1, 3, 5]
print(lst[::3]) #[1, 4]
print(lst[::-1])
print(lst[::-2])
string = "I'm a Good Python Programmer"
new = string.split() 
print(new) # ["I'm", 'a', 'Good', 'Python', 'Programmer']
new = string.split("Good")
print(new) # ["I'm a ", ' Python Programmer']
new = string.split("a")
print(new) # ["I'm ", ' Good Python Progr', 'mmer']
