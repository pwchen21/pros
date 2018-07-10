class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        for x in sorted(nums)[::2]:
            total = total + x
        return total
		
A=Solution()
A.arrayPairSum([1,3,5,9])