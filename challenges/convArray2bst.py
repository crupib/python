class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.key = val
        self.left = left
        self.right = right
class Trunk:
    def __init__(self, prev=None, str=None):
        self.prev = prev
        self.str = str
 
    def showTrunks(self,p):
      if p is None:
        return
      self.showTrunks(p.prev)
      print(p.str, end='')
 
 
    def printTree(self,root, prev, isLeft):
      if root is None:
        return
 
      prev_str = '    '
      trunk = Trunk(prev, prev_str)
      self.printTree(root.right, trunk, True)
 
      if prev is None:
          trunk.str = '———'
      elif isLeft:
          trunk.str = '.———'
          prev_str = '   |'
      else:
          trunk.str = '`———'
          prev.str = prev_str

      self.showTrunks(trunk)
      print(' ' + str(root.key))
      if prev:
          prev.str = prev_str
      trunk.str = '   |'
      self.printTree(root.left, trunk, False)
 
class Solution:     
   def sortedArrayToBST (self,arr):
      if not arr:
        return None
# find middle index
      mid = (len(arr)) // 2
    # make the middle element the root
      root = TreeNode(arr[mid])
    # left subtree of root has all
    # values <arr[mid]
      root.left = self.sortedArrayToBST(arr[:mid])
    # right subtree of root has all
    # values >arr[mid]
      root.right = self.sortedArrayToBST(arr[mid+1:])
      return root
# A utility function to print the preorder
# traversal of the BST
   def preOrder(self, node, temparr):
      if not node:
         return
      temparr.append(node.key)
      #print(node.key)
      self.preOrder(node.left, temparr)
      self.preOrder(node.right, temparr)
#Driver Code
obj = Solution()
arr = [-10,-3,0,5,9]
#arr = [1, 2, 3, 4, 5, 6, 7]
root = obj.sortedArrayToBST(arr)
print("PreOrder Traversal of constructed BST ")
temparr=[]
obj.preOrder(root, temparr)
trunk = Trunk()
trunk.printTree(root, None, False)