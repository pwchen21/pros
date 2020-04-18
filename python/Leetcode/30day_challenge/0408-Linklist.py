class ListNode():
    def __init__(self, val):
        if isinstance(val,int):
            self.val = val
            self.next = None
"""            
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next
    
    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
            return self.__class__.__name__+" {"+"{}".format(self.gatherAttrs())+"}"
"""
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        head = ListNode(head)
        cta = ctb = head
        while cta and ctb.next:
            #print("---while---")
            #print("1. CTA: ", cta)
            #print("2. CTB: ", ctb)
            if ctb.next.next == None:
                return cta.next
            cta = cta.next
            ctb = ctb.next.next
            #print("----------")
            #print("3. CTA: ", cta)
            #print("4. CTB: ", ctb)
        #print("==Ans==")
        print(cta)
        return cta
        
A=Solution()
A.middleNode([1,2,3,4,5])







"""
---while---
1. CTA:  ListNode {val: 1, next: ListNode {val: 2, next: ListNode {val: 3, next: ListNode {val: 4, next: ListNode {val: 5, next: None}}}}}
2. CTB:  ListNode {val: 1, next: ListNode {val: 2, next: ListNode {val: 3, next: ListNode {val: 4, next: ListNode {val: 5, next: None}}}}}
----------
3. CTA:  ListNode {val: 2, next: ListNode {val: 3, next: ListNode {val: 4, next: ListNode {val: 5, next: None}}}}
4. CTB:  ListNode {val: 3, next: ListNode {val: 4, next: ListNode {val: 5, next: None}}}
---while---
1. CTA:  ListNode {val: 2, next: ListNode {val: 3, next: ListNode {val: 4, next: ListNode {val: 5, next: None}}}}
2. CTB:  ListNode {val: 3, next: ListNode {val: 4, next: ListNode {val: 5, next: None}}}
----------
3. CTA:  ListNode {val: 3, next: ListNode {val: 4, next: ListNode {val: 5, next: None}}}
4. CTB:  ListNode {val: 5, next: None}
==Ans==
ListNode {val: 3, next: ListNode {val: 4, next: ListNode {val: 5, next: None}}}
"""