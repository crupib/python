def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say good bye...")
    bye()
def greet2(name):
    print("How are you, " +name+"?")
def bye():
    print("ok bye")

greet("Bill")
