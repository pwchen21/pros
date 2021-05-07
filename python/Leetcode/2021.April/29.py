class Solution:
    def searchRange(self, nums, target):
        if target in nums:
            fst=nums.index(target)
            lst=fst+nums.count(target)-1
            return [fst, lst]
        else:
            return [-1, -1]
        # lsn=len(nums)-1  #Array index
        # if 
        # while nums[lsn] != target:
        #     if nums[lsn] > target:
        #         lsn = lsn // 2
        #         print('0', lsn)
        #     else:
        #         lsn = lsn + (lsn) // 2
        #         print('1', lsn)

        # print('2: Final lsn', lsn)

        # ans=[:]

A=Solution()
A.searchRange([2,3,4,8,8,8,9,11], 8)