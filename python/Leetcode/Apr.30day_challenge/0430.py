[0,1,0,0,1,0,null,null,1,0,0]
[0,1,0,1]

[0,1,0,0,1,0,null,null,1,0,0]
[0,1,1]

[4,null,2,7,5,3,4,4]
[4,2,7,4]

=======
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        #print('root:' , root)
        #print('root.val:', root.val)
        #print('root.left.val', root.left.val)
        ans = True
        ntlv = False
        lr=root
        rr=root
        if root.val == arr[0]: 
            for x in range(1,len(arr)):
                print('======================')
                print('ckp1-x-arr[x]:', x, arr[x])
                print('ckp2-root now:', root)
                if lr.left != None or rr.right != None:
                    if lr.left != None and lr.left.val == arr[x]:
                        print('left:', lr.left.val) 
                        lr = lr.left                 
                        print('reset root: ', lr)
                        ans = True
                        
                    if rr.left != None and rr.right.val == arr[x]:
                        print('right', rr.right.val)
                        rr = rr.right
                        print('reset root: ', rr)
                        ans = True
                else:
                    ans = False
        
        print("==End Root===")
        print(root)
        if lr.left or rr.right:
            ntlv == True
            
        print('ans:', ans , ' ntlv:', ntlv)
        return ans==True and ntlv==False
		
		
==================

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        #print('root:' , root)
        #print('root.val:', root.val)
        #print('root.left.val', root.left.val)
        ans = True
        ntlv = False
        if root.val == arr[0]: 
            for x in range(1,len(arr)):
                print('======================')
                print('ckp1-x-arr[x]:', x, arr[x])
                print('ckp2-root now:', root)
                if root.left != None or root.right != None:
                    if root.left != None and root.left.val == arr[x]:
                        print('left:', root.left.val) 
                        root = root.left                 
                        print('reset root: ', root)
                        ans = True
                        
                    if root.right != None and root.right.val == arr[x]:
                        print('right', root.right.val)
                        root = root.right
                        print('reset root: ', root)
                        ans = True
                else:
                    ans = False
        
        print("==End Root===")
        print(root)
        if root.left or root.right:
            ntlv == True
            
        print('ans:', ans , ' ntlv:', ntlv)
        return ans==True and ntlv==False
		
		

                