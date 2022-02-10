class Solution:
    def findMaxAverage(self, nums, k):
        
        max_now=sum(nums[0:k])
        for x in range(1, len(nums)-k+1):
            print(x)
            if sum(nums[x:x+k]) > max_now:
                max_now = sum(nums[x:x+k])
                
        print(max_now/k)
        return max_now/k

A=Solution()
A.findMaxAverage([1,12,-5,-6,50,3]      , 4)