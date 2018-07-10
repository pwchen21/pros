class Solution(object):
    def maxSubArray(self, nums):
		M=nums[0]
		C=nums[0]
		for x in nums[1:]:
			#print "C+x, x: ", C+x, x
			C=max(C+x, x)
			#print 'C:', C
			#print "---"
			#print "C, M:", C, M
			M=max(C,M)
			#print M
		return M
		

A=Solution()
A.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])