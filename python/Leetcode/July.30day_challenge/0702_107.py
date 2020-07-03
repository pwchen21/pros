class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        queue = [root]
        res = [[root.val]]
        
        while queue:
            child=[]
            for node in queue:                
                if node.left:
                    child.append(node.left)                
                if node.right:
                    child.append(node.right)                
            if not child:
                    break
                
            queue = child
            #print(queue)                
            res.append([node.val for node in queue])
            #print(res)
        
        return(res[::-1])