class Solution(object):
    def testRec(self, n):
		if n > 0:
			print n
		else:
			self.testRec(abs(n))
			print 'yes'
			
A=Solution()
A.testRec(10)
A.testRec(-5)