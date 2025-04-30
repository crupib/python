import stack as stk

stack=stk.Stack()
print("push ",'Red')
stack.push('Red')
print("push ",'Green')
stack.push('Green')
print("push ",'Blue')
stack.push('Blue')
print("push ",'Yellow')
stack.push('Yellow')
print("popped ", stack.pop())
print("is stack empty",stack.isEmpty())
while stack.isEmpty() == False :
 print("popped ", stack.pop())
