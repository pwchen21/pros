class Solution(object):
    def checkPossibility(self, nums):
		de=0
		co=0
		print 'len(nums)', len(nums)
		while co < len(nums)-1:
			#print 'while'
			#print 'nums[co]', nums[co]
			#print 'nums[co+1]', nums[co+1]
			if nums[co] > nums[co+1]:
				de+=1	
				#print 'de', de
			co+=1
			#print 'co', co
		print de
		print de < 2
A=Solution()
A.checkPossibility([3,2,1])