class Solution:
    def search(self, nums, target):
        start=0
        end=len(nums)
        while start < end:
            mid=start+(end-start)//2
            print(start, end, mid)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end=mid
            if nums[mid] < target:
                start+=1                
        return -1

A=Solution()
A.search([-1,0,3,5,9,12], 3)