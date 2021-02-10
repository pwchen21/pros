class Solution:
    def minOperations(self, nums,x):
        start, end, target, max_len = 0, 0, sum(nums)-x, -1
        if target >= 0:
            while end < len(nums):
                target -= nums[end]
                end += 1
                while target < 0:
                    target += nums[start]
                    start += 1
                if target == 0:
                    max_len = max(max_len, end-start)
        return len(nums) - max_len if max_len > -1 else -1

A=Solution()
A.minOperations([3,2,20,1,1,3], 10)