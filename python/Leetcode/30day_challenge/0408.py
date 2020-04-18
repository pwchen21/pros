class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        head = ListNode(head)
        cta = ctb = head
        #print(cta.val)
        #print(ctb.val)
        while cta and ctb.next:
            print(cta.val)
            print(ctb.val.next)
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
        #print(cta)
        return cta
        
A=Solution()
A.middleNode([1,2,3,4,5])
