class treeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
	def insertLeft(self, val):
		if self.left == None:
			self.left = treeNode(val)
		else:
			self.left.insertLeft(val)
    
	def insertRight(self, val):
		if self.right == None:
			self.right = treeNode(val)
		else:
			self.right.insertRight(val)
			 
sampleTree = treeNode(5)
sampleTree.insertRight(7)
sampleTree.insertRight(8)
sampleTree.insertLeft(3)
sampleTree.insertLeft(2)
sampleTree.right.insertLeft(6)
sampleTree.left.insertRight(4)

print(sampleTree)