class Solution(object):
	def plusOne(self, digits):
		digits.reverse()
		print digits
		sum=0
		ans=[]
		for x in range(len(digits)):
			print 'x',x
			print '10^base', 10**x
			print 'dix', digits[x]
			print 'add', (digits[x]*(10**x))
			sum=sum+(digits[x]*(10**x))
			print 'sum', sum
			
		for x in str(sum+1):
			ans.append(int(x))
		
		print ans
A=Solution()
A.plusOne([30,8])