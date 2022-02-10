class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        Sum = 0
        diff = 1000000
        print(nums)

        for i in range(n - 2):
            print('i now:', i)
            l = i + 1 
            r = n - 1 
            print('L:', l, ' R:', r)
            
            while l < r:
                value = nums[i] + nums[l] + nums[r]
                print(value,' pick:', i, l, r," - ", nums[i], nums[l], nums[r])
                print('diff', diff)
                if abs(value - target) < diff:
                    diff = abs(value - target)
                    Sum = value

                elif value < target:
                    l += 1

                else:
                    r -= 1 
        print(Sum)
        return Sum


A=Solution()
A.threeSumClosest([1,1,-1,-1,3], 3)