class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def isSameTree(self, p, q):
	
	if not p: return not q
	if not q: return not p
    
	if p.val!=q.val: 
		return False
	else: 	
		return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
		
		
p=[1,2,3,4,5]
q=[2,3,4,5,6]
Solution.isSameTree(p,q)