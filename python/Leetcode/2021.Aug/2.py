class Solution:
    def twoSum(self, nums, target):
        ans=[]
        for x in range(len(nums)):
            if (target - nums[x]) in nums[x+1:]:
                #print('1')
                for y in range(x+1, len(nums), 1):
                    #print('2')
                    if target-nums[x] == nums[y]:
                        #print('3')
                        ans.append(x)
                        ans.append(y)
                        print(ans)
                        return(ans)

A=Solution()
A.twoSum([2,7,11,15], 9)
        