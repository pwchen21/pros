class Solution:
    def addDigits(self, num: int) -> int:
        tmp=num
        while len(str(num)) > 1:
            tmp=0
            for x in str(num):
                tmp+=int(x)
            num=tmp
        print(tmp)

A=Solution()
A.addDigits(38)