class Solution:
    def minOperations(self, nums, x):
        self.ctlv(nums, x)

    def ctlv(self, nums, x):
    	tx=x

    	RL, RC=[nums.pop(0)], 0
    	LL, LC=[nums.pop()], 0
    	if (tx - nums[0] == 0) & (tx - nums[-1] == 0):
    		return min(RC, LC)
    	elif:
    		rt = self.ctlv(RL, tx-nums[0])
    		lt = self.ctlv(LL, tx-nums[-1])
    	elif tx-:

    	else:
    		return -1


A=Solution()
A.minOperations([3,2,20,1,1,3], 10)
