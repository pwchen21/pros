class Solution:
    def threeSum(self, nums):
        nums.sort()
        n, result = len(nums), []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue

            target = -nums[i]
            beg, end = i + 1, n - 1

            while beg < end:
                if nums[beg] + nums[end] < target:
                    beg += 1
                elif nums[beg] + nums[end] > target:
                    end -= 1
                else:
                    result.append((nums[i], nums[beg], nums[end]))
                    beg += 1
                    end -= 1

        return set(result)


A=Solution()
A.threeSum([-12,-1,4,-14,0,10,7,-7,-6,9,6,-2,7,13,9,-1,4,12,9,4,14,0,-4,0,0,10,2,-7,7,-4,-11,10,2,8,4,-12,-4,-12,-4,-3,12,9,11,4,-1,-3,10,-12,-6,-4,-1,-14,3,2,-7,-11,-3,10,-11,-10,13,-15,7,0,0,-4,-5,11,0,-2,-14,-11,-8,12,1,-1,-14,-12,-6,-5,0,9,-4,-12,-4,4,14,9,-9,10,14,-11,10,6,-3,-4,10,-1,14,-13,13,7,-9,12,4,-1,-4,5,3,6,8,10,0,11,13,11,-7,5,-3,-1,0,-4,-4,-4,10,0])