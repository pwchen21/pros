class Solution(object):
    def removeElement(self, nums, val):
		cntval=nums.count(val)
		x=0
		while x < cntval:
			nums.remove(val)
			x=x+1
		print nums
		#print nums.pop(val)
        
		
A=Solution()
A.removeElement([3,2,2,3], 3)