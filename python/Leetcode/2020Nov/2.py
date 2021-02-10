class Solution:
    def shuffle(self, nums):
    	ans=[]
    	temp=0
    	for x in nums:
    		temp+=x
    		ans.append(temp)
    		print(ans)


A=Solution()
A.runningSum([1,2,3,4])