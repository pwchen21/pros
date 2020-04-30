class Solution:
    def maxSubArray(self, nums):
        t1=nums[0]
        t2=nums[0]
        for i in range(1, len(nums)):
            t1=max(t1+nums[i], nums[i])
            t2=max(t1, t2)
            print(t1,t2)
        print(t2)
        
A=Solution()
A.maxSubArray([-57,9,-72,-72,-62,45,-97,24,-39])