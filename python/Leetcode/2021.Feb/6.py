 #Self Solution w/t wrong ans
        ans=[]
        def chk(node):
            while node.right:
                #print('w:', node)
                ans.append(node.right.val)
                chk(node.right)
                return ans

        
        #print(root)
        if root:
            ans.append(root.val)
            return chk(root)
        else:
            return root