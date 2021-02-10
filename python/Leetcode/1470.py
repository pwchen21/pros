class Solution:
    def shuffle(self, nums, n):
    	ans=[]
    	le=len(nums)
    	for x in range(le-n):
    		#print(x)
    		ans.append(nums[x])
    		if x+n < le:
    			#print(nums[x+n])
    			ans.append(nums[x+n])
    	print(ans)

A=Solution()
A.shuffle( [1,2,3,4,4,3,2,1], 4)