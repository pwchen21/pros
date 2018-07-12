class Solution(object):
	def shoppingOffers(self, A, B):
		self.A=A
		self.B=B
		self.pri(A,B)
	
	def pri(self, x, y):
		print self.A
		print self.B
		print x
		print y
		
		C=self.A+1
		D=self.B+1
		if C > 12:
			print 'big'
		else:
			self.pri(C,D)
		
		
		


A=Solution()
A.shoppingOffers(7,8)