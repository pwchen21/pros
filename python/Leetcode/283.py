class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        wh = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[wh] = nums[i]
                wh += 1
                print(nums)
        for i in range(wh, len(nums)):
            nums[i] = 0


A=Solution()
A.moveZeroes([0,1,3,0,28,2,0,1])