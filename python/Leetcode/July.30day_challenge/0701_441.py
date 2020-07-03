class Solution(object):
    def arrangeCoins(self, n):
        ct = 1
        rn = n
        while rn - ct >= 0:
            rn -= ct
            ct += 1
            print(ct, rn)
            
        print('ans:', ct)

A=Solution()
A.arrangeCoins(9)