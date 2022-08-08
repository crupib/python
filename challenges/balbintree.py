class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.key = val
        self.left = left
        self.right = right
class Solution:     
   def height(self,root):
     
    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(self.height(root.left), self.height(root.right)) + 1
   def isBalanced(self,root):
     
    # Base condition
    if root is None:
        return True
 
    # for left and right subtree height
    lh = self.height(root.left)
    rh = self.height(root.right)
 
    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and self.isBalanced(
        root.left) is True and self.isBalanced( root.right) is True:
        return True
 
    # if we reach here means tree is not
    # height-balanced tree
    return False
 

#Driver Code
obj = Solution()
obj2 = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
if obj.isBalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")
# second tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.right.right = TreeNode(3)
root2.left.left.left =TreeNode(4) 
root2.left.left.right =TreeNode(4) 
if obj2.isBalanced(root2):
    print("Tree is balanced")
else:
    print("Tree is not balanced")
