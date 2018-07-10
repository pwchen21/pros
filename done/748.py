class Solution(object):
    def dominantIndex(self, nums):
		print 'nums:', nums
		maxn=max(nums)
		co=nums[:]
		co.remove(maxn)
		print 'copy nums:', co
		colen=len(co)
		print 'len of co', colen
		for x in co:
			print 'x:',x
			if 2*x <= maxn:
				colen = colen - 1
				print 'colen=',colen
			else:
				print -1
				return -1
		if colen == 0:
			print '4', nums
			print nums.index(maxn)
			return nums.index(maxn)

A=Solution()
A.dominantIndex([6,3,1,2])