import math

class Solution(object):
    def judgeSquareSum(self, c):

		for x in range(0,int(math.sqrt(c))+1):
			#print 'x', x
			#print 'y', math.sqrt(c-x*x)
			#print math.sqrt(c-x*x).is_integer()
			if math.sqrt(c-x*x).is_integer():
				print True
		return False

			
A=Solution()
A.judgeSquareSum(0)