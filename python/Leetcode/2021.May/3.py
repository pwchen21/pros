class Solution:
    def runningSum(self, nums):
        # ans=[nums[0]]
        # for x in range(1, len(nums), 1):
        #     print('x', x, ans[x-1], nums[x])
        #     ans.append(ans[x-1]+nums[x])
            
        # print(ans)

        for i in range(1, len(nums)):
            print(i, nums[i-1], nums[i])
            nums[i] = nums[i-1] + nums[i]
        return nums

A=Solution()
A.runningSum([1,2,3,4])
            
