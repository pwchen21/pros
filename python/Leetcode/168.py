class Solution(object):
    def convertToTitle(self, n):
		res=[]
		if n == 0:
			print 0
		else:
			print 'n:' , n
			print (self.convertToTitle((n - 1) / 26)), (chr((n - 1) % 26 + ord('A')))
			print 'a:', (chr((n - 1) % 26 + ord('A')))
			res.append((chr((n - 1) % 26 + ord('A'))))
		print res
			

A=Solution()
A.convertToTitle(221)