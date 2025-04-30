
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.key = val
        self.left = left
        self.right = right
class Solution:     
   def minDepth(self, root):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    if root is None:
        return 0
     
    # Base Case : Leaf node.This accounts for height = 1
    if root.left is None and root.right is None:
        return 1
     
    # If left subtree is Null, recur for right subtree
    if root.left is None:
        return self.minDepth(root.right)+1
     
    # If right subtree is Null , recur for left subtree
    if root.right is None:
        return self.minDepth(root.left) +1
     
    return min(self.minDepth(root.left), self.minDepth(root.right))+1
 

#Driver Code
obj = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(obj.minDepth(root))

root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
print(obj.minDepth(root))