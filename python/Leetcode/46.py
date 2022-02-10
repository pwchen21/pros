class Solution:
    def permute(self, nums):
        res=[]
        def rec(nums, cur_lst):
            if len(nums) == len(cur_lst):
                res.append(cur_lst[:])

            for i in nums:
                if i not in cur_lst:
                    cur_lst.append(i)
                    rec(nums, cur_lst)
                    cur_lst.pop()   
        rec(nums, [])
        print(res)

A=Solution()
A.permute([1,2,3])