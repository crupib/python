class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.key = val
        self.left = left
        self.right = right
class Solution:     
   def maxDepth (self,root):
      if root == None:
        return 0
      leftDepth = self.maxDepth(root.left)
      rightDepth = self.maxDepth(root.right)
      # Choose the larger one and add the root to it.
      if leftDepth > rightDepth:
        return leftDepth + 1
      else:
       return rightDepth + 1

#Driver Code
obj = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.maxDepth(root))
root = TreeNode(1)
root.right = TreeNode(2)
print(obj.maxDepth(root))
