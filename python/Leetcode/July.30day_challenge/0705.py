class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans=0
        bx=bin(x)[2:]
        by=bin(y)[2:]
        m=max(len(bx), len(by))
        if m == len(bx):
            by='0'*(m-len(by))+by
        else:
            bx='0'*(m-len(bx))+bx
        
        for i in range(m):
            if bx[i] != by[i]:
                ans+=1
                
        print(ans)
        return ans
        
A=Solution()
A.hammingDistance(1, 4)