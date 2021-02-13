def convertBST(self, root: TreeNode) -> TreeNode:
    self.Sum = 0
    return self.reverse_inorder(root)
    
    
def reverse_inorder(self,root):
    if root == None:
        return
    else:
        self.reverse_inorder(root.right)
        self.Sum += root.val
        root.val = self.Sum
        self.reverse_inorder(root.left)
        return root