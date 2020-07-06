class Solution:
    def isUgly(self, num):
        for x in [2,3,5]:
            while num % x == 0:
                num /= x
        if num == 1:
            return True
                
    def nthUglyNumber(self, n: int) -> int:
        ansl=[1]
        ct=2
        #print(len(ansl), n)
        while len(ansl) <= n-1:
            if self.isUgly(ct) == True:
                ansl.append(ct)
            ct += 1
            print(ansl)
            
        print(ansl[-1])
         
A=Solution()
A.nthUglyNumber(1690)         