# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self. recursive_inorder (root, res)
        print(res)
        return res
    def recursive_inorder(self, root, res):#recursive inorder traversal
        if root:
            self.recursive_inorder(root.left, res)
            res.append(root.val)
            self.recursive_inorder(root.right, res)
            
            
if __name__ =='__main__':
    S = Solution()
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    
    root = l1
    l1.left = None
    l1.right = l2
    l2.left = l3
    S.inorderTraversal(root)
