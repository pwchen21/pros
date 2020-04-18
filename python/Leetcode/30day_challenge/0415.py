class Solution:
    def productExceptSelf(self, nums):
        ans=[]
        left  = 1
        right = 1
        for x in range(len(nums)):
            ans.append(left)
            left *= nums[x]
        
        for y in range(len(nums)-1, -1, -1):
            ans[y] *= right
            right *= nums[y]
        
        print(ans)
        return ans
        
A=Solution()
A.productExceptSelf([1,2,3,4])