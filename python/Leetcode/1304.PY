class Solution:
    def sumZero(self, n):
    	ans=[]
    	tmp=1
    	if n == 0:
    		return []
    	
    	while len(ans) <= n-2:
    		ans.append(tmp)
    		ans.append(-tmp)
    		tmp+=1
    		print(ans)
    	
    	if len(ans) < n:
    		ans.append(0)

    	print(ans)

A=Solution()
A.sumZero(0)
print('-----')
A.sumZero(6)  
print('----')
A.sumZero(5)

