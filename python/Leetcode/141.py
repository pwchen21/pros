class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
 
   def hasCycle(self, head):
        try:
            
			fast = head.next.next
            slow = head.next
            
            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            
            print True
        except:
            print False
			
A=Solution()
A.hasCycle([3,1,9, 1,3])