class Solution:
    def hammingWeight(self, n):
        res = 0
        while n>0:
            res += n&1
            n = n>>1
        print(res)


A=Solution()
A.hammingWeight(10111)