class Solution:
    def maxArea(self, height):
    	# Correct Answer, but time limit exeed
        ans=0
        h=len(height)-1
        for x in range(len(height)):
        	print(x)
        	for y in height[-1:x:-1]:
        		print(' y', y)
        		print(' height:', min(y, height[x]))
        		print(' width', (h-x))
        		if (h-x)*min(y, height[x]) > ans:
        			ans = (h-x)*min(y, height[x])
        			print('ans', ans)
        		h-=1
        	h=len(height)-1

        print('Final Answer:', ans)
A=Solution()
A.maxArea([3,9,3,4,7,2,12,6])