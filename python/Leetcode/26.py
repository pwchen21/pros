class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return len(nums)
        
        t=nums[0]
        
        for x in nums[1:]:
            if x == t:
                nums.remove(x)
            else:
                t=x
        
        return len(nums)


A=Solution()
A.removeDuplicates([1])
        