# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:       
        def dfs(p, q):
            #When two binary trees are empty
            if p == None and q == None:
                return True
            #When only one of two binary trees is empty
            elif p == None or q == None:
                return False
            #If the binary tree is not empty, compare the value
            elif p.val == q.val:
#When the value of the root node is the same, continue to judge the value of the left and right subtrees
                return dfs(p.left, q.left) and dfs(p.right, q.right)
#If the value is different, false is returned
            return False
        return dfs(p, q)
#Driver Code
obj = Solution()
root1 = TreeNode(1)
root2 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
if (obj.isSameTree(root1,root2)) :
    print("Trees are identical")
else:
    print("Trees are not the same")
root1 = TreeNode(1)
root2 = TreeNode(1)
root1.left = TreeNode(2)
root2.right = TreeNode(2)
if (obj.isSameTree(root1,root2)) :
    print("Trees are identical")
else:
    print("Trees are not the same")