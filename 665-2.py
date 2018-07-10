class Solution(object):
    def checkPossibility(self, nums):
        de=0
        co=0
        while co < len(nums)-1:
			if nums[co] > nums[co+1]:
				de+=1
			co+=1
        print de <= 1
		
A=Solution()
A.checkPossibility([3,4,2,3])