class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = self.dep(root.left) + self.dep(root.right)
        return max(ans, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))
 
    def dep(self, node):
        if not node:
            return 0
        return max(self.dep(node.left), self.dep(node.right)) +1
    

A=Solution()
A.diameterOfBinaryTree([1,2,3,4,5])