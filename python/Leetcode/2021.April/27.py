class Solution:
    def isPowerOfThree(self, n):
        while n > 3:
            n=n/3

        #print(n)
        print (n/3 == 1)
        return (n/3 == 1)
A=Solution()
A.isPowerOfThree(45)
A.isPowerOfThree(0)
A.isPowerOfThree(2)
A.isPowerOfThree(27)
