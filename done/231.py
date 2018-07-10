class Solution(object):
    def isPowerOfTwo(self, n):
			print bin(n)[2:].count('1')  == 1

A=Solution()
A.isPowerOfTwo(30)
A.isPowerOfTwo(1)
A.isPowerOfTwo(16)
A.isPowerOfTwo(25)