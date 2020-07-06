class Solution:
    def plusOne(self, digits):
        tmp=[]
        ans=0
        res=[]
        for x in digits:
            tmp.append(str(x))
        
        ans = str(int(''.join(tmp))+1)
        print(ans)
        
        for y in ans:
            res.append(int(y))
            
        print(res)
        return res
        
A=Solution()
A.plusOne([1,2,3,4,9])