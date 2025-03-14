from tkinter.tix import Tree


class GFG :
    @staticmethod
    def main( args) :
        tree = BST()
        tree.insert(1)
        tree.insert(2)
        tree.insert(15)
        tree.insert(20)
        tree.insert(10)
        tree.insert(40)
        tree.insert(60)
        tree.inorder()
class Node :
    left = None
    val = 0
    right = None
    def __init__(self, val) :
        self.val = val
class BST :
    root = None
    def insert(self, key) :
        node = Node(key)
        if (self.root == None) :
            self.root = node
            return
        prev = None
        temp = self.root
        while (temp != None) :
            if (temp.val > key) :
                prev = temp
                temp = temp.left
            elif(temp.val < key) :
                prev = temp
                temp = temp.right
        if (prev.val > key) :
            prev.left = node
        else :
            prev.right = node
    def inorder(self) :
        temp = self.root
        stack =  []
        while (temp != None or not (len(stack) == 0)) :
            if (temp != None) :
                stack.append(temp)
                temp = temp.left
            else :
                temp = stack.pop()
                print(str(temp.val) + " ", end ="")
                temp = temp.right
     
if __name__=="__main__":
    GFG.main([])
     
    # This code is contributed by rastogik346.