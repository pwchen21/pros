# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        print(len(set(vals)) == 1)
			
#T=[1,1,1,1,'Null',2,1]
T=[1,1,1,1,1,1,1]
A=TreeNode(T)
Solution.isUnivalTree(T[0],A)