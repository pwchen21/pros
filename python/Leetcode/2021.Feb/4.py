from collections import Counter
''' 
#Solution 1
class Solution:
	def findLHS(self, nums: List[int]) -> int:
		ct=Counter(nums)
		res = 0
		for x in ct:
			#print(x)
			if x+1 in ct:
				res=max(res, ct[x]+ct[x+1])
				#print(res)
		return res
'''

#Solution 2
class Solution:
	def findLHS(self, nums):
		ct = Counter(nums)
		res = 0
		for i, n in ct.items():
			if i+1 in ct:
				res = max(res, n+ct[i+1])

		print(res)

A=Solution()
A.findLHS([1,2,3,4,2,3,1])