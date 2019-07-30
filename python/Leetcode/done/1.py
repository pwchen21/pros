class Solution(object):
    def twoSum(self, nums, target):	
		res=[]
		for x in nums:
			if (target - x) in nums:
				if x != target - x:
					print  [nums.index(x), nums.index(target-x)]
				else:
					for (i, data) in enumerate(nums):
						if data == x:
							res.append(i)
							if len(res) == 2:
								print res
								#print 'index:', i
								#print 'data:', data


A=Solution()
A.twoSum([2,3,4,2,9], 4)					