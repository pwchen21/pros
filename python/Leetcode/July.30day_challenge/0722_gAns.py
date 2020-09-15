class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None
        
        queue=[]
        ans=[]
        queue.append(root)
        c=0
        while len(queue):
            c=c+1
            r=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                r.append(node.val)
                
                if node.left!=None:
                    queue.append(node.left)
                
                if node.right!=None:
                    queue.append(node.right)
            if c%2==0:
                r=r[::-1]
                ans.append(r)
            else:
                ans.append(r)
        return ans