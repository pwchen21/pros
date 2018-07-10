class Solution(object):
    def isHappy(self, n):
		tot=n
		def sqr(n):
			tot=0
			for x in str(n):
				sq=int(x)**2			
				tot = tot+sq
				print '2:', tot	
			return tot

		#if len(str(tot)) == 1:
		#	tot=str('0')+str('tot')
			
		while len(str(tot))>1:
			tot=sqr(tot)
		
		print tot==1
		
'''
class Solution(object):
    def isHappy(self, n):
		tot=n
		def sqr(n):
			tot=0
			for x in str(n):
				print 'x', x
				sq=int(x)**2			
				tot = tot+sq
				print '2:', tot	
			return tot
		print 'len(str(tot))', len(str(tot))
		
		if len(str(tot)) == 1:
			print True
		
		while len(str(tot))>1:
			print '1:', tot
			tot=sqr(tot)
		print '3',tot
		
		print tot==1
'''		
A=Solution()
A.isHappy(7)