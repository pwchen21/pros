class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i<len(preorder) and  preorder[i] < root.val:
            i+=1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
        
A=Solution()
A.bstFromPreorder([8,5,1,7,10,12])