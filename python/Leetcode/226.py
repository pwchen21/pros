class Solution(object):
    def invertTree(self, root): 
        if root:
            invert = self.invertTree
            root.left, root.right = invert(root.right), invert(root.left)
            return root
        

p=Solution()
p.invertTree('[4,2,7,1,3,6,9]')

