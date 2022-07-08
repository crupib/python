class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.key = val
        self.left = left
        self.right = right
class Solution:     
   def isMirror(self,root1, root2):
    # If both trees are empty, then they are mirror images
      if root1 is None and root2 is None:
        return True
      if (root1 is not None and root2 is not None):
        if root1.key == root2.key:
            return (self.isMirror(root1.left, root2.right)and
                    self.isMirror(root1.right, root2.left))
 
    # If none of the above conditions is true then root1
    # and root2 are not mirror images
      return False
 
 
   def isSymmetric(self,root): 
        # Check if tree is mirror of itself
        return self.isMirror(root, root)
 

#Driver Code
obj = Solution()

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

if (obj.isSymmetric(root1)) :
    print("Trees are symmetric")
else:
    print("Trees are not the symmetric")
