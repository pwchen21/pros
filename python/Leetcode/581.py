class Solution(object):
    def findUnsortedSubarray(self, nums):
        if len(nums) <2: 
            return 0
        
        prev = nums[0]
        end = 0
        # find the largest index not in place
        for i in range(0, len(nums)):
            print("R", i, nums[i])
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]
            print(" Right:", end, prev)

        start = len(nums) - 1
        prev = nums[start]
        # find the smallest index not in place
        for i in range(len(nums)-1, -1, -1):
            print("L", i, nums[i])

            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]

            print(" Left:", start, prev)
        
        if end != 0:
            return end - start + 1
        else: 
            return 0

A=Solution()
A.findUnsortedSubarray([2,6,4,8,10,9,15])