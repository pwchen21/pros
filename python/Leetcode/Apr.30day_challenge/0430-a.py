class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        l = len(arr)
        i = 0
        return self.ckpath(root, arr, l, i)
    
    def ckpath(self, root, arr, l, i):
        if root is None:
            return l == 0
        if (i == l-1) and (root.left == None and root.right == None) and (root.val == arr[i]):
            return True
        if (i < l) and (root.val ==  arr[i]):
            return (self.ckpath(root.left, arr, l, i+1) or (self.ckpath(root.right, arr, l, i+1)))