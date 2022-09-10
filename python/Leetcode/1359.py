class Solution:
    def countOrders(self, n: int) -> int:
        mod=10**9+7
        ans, pre_total, pre=1, 1, 1 
        #pre_total is f(i-1), pre=sum(i)
        for i in range(2, n+1):
            tmp=(i*4-3)+pre
            ans=pre_total*tmp
            # i*4-3 => (i*2-1)(i*2-2)
            pre_total=ans
            pre=tmp
            
        return ans % mod
    
        
A=Solution()
A.countOrders()