class Solution:
    def numberOfSteps (self, num: int) -> int:
        ct=0
        while num > 0:
            #print(ct, '-----w:', tr)
            ct+=1
            if num % 2 == 1:
                num -= 1
            else:
                num /= 2

        print(ct, 'ans: ', ct)
        return ct
                
        
A=Solution()
A.numberOfSteps(8)
A.numberOfSteps(14)