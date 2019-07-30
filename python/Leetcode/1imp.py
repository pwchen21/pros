class Solution(object):
    def twoSum(self, nums, target):	
		D={}
		for i, data in enumerate(nums):
			D[data]=i
			

A=Solution()
A.twoSum([2,3,4,2,9], 4)					