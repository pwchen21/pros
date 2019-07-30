class Solution(object):
    def searchInsert(self, nums, target):
		if target in nums:
			#print '1'
			#print nums.index(target)
			return nums.index(target)
		elif nums[-1] < target:
			print len(nums)
			return len(nums)
		elif nums[0] > target:
			#print '2'
			#print 0
			return 0
		else:
			for x in nums[:-1]:
				print 'x', x
				if x < target:
					if nums[nums.index(x)+1] > target:
						#print 'xx',nums.index(x)+1
						#print '3'
						#print nums.index(x)+1
						return nums.index(x)+1

A=Solution()

print "==case1:==="
A.searchInsert([1], 0)
print "==case2:==="
A.searchInsert([0,1,2,3,4],2)
print "==case3:==="
A.searchInsert([0,1,3,4],2)
print "==case4:==="
A.searchInsert([0,1,3,4],7)