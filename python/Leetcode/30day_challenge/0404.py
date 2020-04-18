class Solution:
    def moveZeroes(self, nums):
        print('Start')
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        print(nums)
A=Solution()
A.moveZeroes([0,1,0,3,12])