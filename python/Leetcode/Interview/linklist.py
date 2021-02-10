 https://www.youtube.com/watch?v=tk6fo3Z-qkQ&ab_channel=SuboptimalEngineer

        '''
        Solution from other people
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next
        '''
        #print(head)
        #print(n)
        # ls=[]
        # node=head
        
        # while node:            
        #     ls.append(node.val)
        #     node=node.next
        
        # rm=(ls[-n])
        # print('rm', rm)
        
        # del 
        
    '''
        ans=ListNode(ls[0])
        print('1', ans)
        for x in ls[1:]:
            ans=self.lk(x, ans)
            print(ans)
            
    def lk(self, addx, listw):
        listw.next=addx
        print('n', listw)
        return(listw.next)
    '''     
        # while head.next != None:
        #     print('here')
        #     if head.val==ls[-n]:
        #         head.val=head.next.val
        #         head=head.next
        #         print('1', head)
        #     else:
        #         head=head.next
        #         print('2', head)
        # return head
            