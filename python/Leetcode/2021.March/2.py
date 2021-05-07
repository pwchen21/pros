class Solution:
    def findErrorNums(self, nums):
        '''
        print('0', nums)
        _nums = [0] + [1] * len(nums)
        print('1', _nums)
        for x in nums:
            _nums[x] = _nums[x] - 1
            print('2', _nums[x])
        return [_nums.index(-1), _nums.index(1)]
        '''
        temp = sum(set(nums))
        print('temp', temp)
        rep = sum(nums) - temp
        print('rep', rep)
        mis = sum(range(len(nums)+1)) - temp
        print(mis)
        return [rep, mis]

A=Solution()
A.findErrorNums([1,2,3,3])
print("=======")
A.findErrorNums([3,2,2])
print("=======")
A.findErrorNums([2,3,4,4])
