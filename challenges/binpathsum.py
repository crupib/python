
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.key = val
        self.left = left
        self.right = right
class Solution:     
   def hasPathSum(self, root, s):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    ans = 0
    if root == None:
       return 0
    subSum = s - root.key
 
    # If we reach a leaf node and sum becomes 0, then
    # return True
    if(subSum == 0 and root.left == None and root.right == None):
        return True
 
    # Otherwise check both subtrees
    if root.left is not None:
        ans = ans or self.hasPathSum(root.left, subSum)
    if root.right is not None:
        ans = ans or self.hasPathSum(root.right, subSum)
 
    return ans
 

#Driver Code
obj = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.right = TreeNode(2)
root.left.left.left = TreeNode(7)
root.right = TreeNode(8)
root.right.right = TreeNode(4)
root.right.left = TreeNode(13)
root.right.right.right = TreeNode(1)
s = 22
if obj.hasPathSum(root, s):
        print("There is a root-to-leaf path with sum %d" % (s))
else:
        print("There is no root-to-leaf path with sum %d" % (s))
root = None
s = 0
if obj.hasPathSum(root, s):
    print("There is a root-to-leaf path with sum %d" % (s))
else:
    print("There is no root-to-leaf path with sum %d" % (s))

