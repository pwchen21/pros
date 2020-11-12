class Solution(object):
    def moveZeroes(self, nums):
		print nums
		for x in nums:
			if x == 0:
				key = 0
			else:
				key = 1
			nums.sort(key)
		#nums.sort(key=lambda x: 1 if x==0 else 0 )
		'''
		for x in nums:
			if x == 0:
				nums.remove(0)
				nums.append(0)
		'''
		print nums

P=Solution()
P.moveZeroes([0,1,0,3,12])
P.moveZeroes([0,1,0,0,2,0,0,3,12])