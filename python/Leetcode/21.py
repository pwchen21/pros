        sta = ListNode(0)
        print(sta)
        ans = sta
        print(ans)
        
        while list1 and list2:
            if list1.val <= list2.val:
                ans.next=list1
                list1=list1.next
            else:
                ans.next=list2
                list2=list2.next
            ans = ans.next            
        if list1:
            ans.next=list1.next
        else:
            ans.next=list2.next
            
        print(sta.next)