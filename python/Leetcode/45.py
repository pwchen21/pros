class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = end = step = 0
        while end < len(nums)-1:
			print 'end:', end
			print 'len(nums):', nums
			print 'max:', max([i+nums[i] for i in range(start, end+1)])
			print '================='
			print [i+nums[i] for i in range(start, end+1)]
			print '================='
			start, end = end+1, max([i+nums[i] for i in range(start, end+1)])
			
			step += 1 
		#print step
		
A=Solution()
A.jump([2,3,1,1,4])