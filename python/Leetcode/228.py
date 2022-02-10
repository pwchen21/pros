class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return nums
        
        ans = [nums[0]]
        re = True
        ct = 0
        index = 1
        
        while index < len(nums):
            print(index,":",  nums[index])
            if nums[index] - nums[index-1] == 1:
                re = False
                ct += 1
            else:
                if ct > 0:
                    ans[-1] = str(ans[-1]) + '->' + str(nums[index-1])
                    ct = 0
                    re = True
                    
            if re == True:
                print('h')
                ans.append(str(nums[index]))
                    
            index+=1
        if ct > 0:
            ans[-1] = ans[-1]+'->'+ans[index]
            
        print(ans)
        return ans

A=Solution()
A.summaryRanges([0,1,2,4,5,7])