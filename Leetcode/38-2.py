import itertools

class Solution:
	def countAndSay(self, n):
		s = '1'
		for _ in range(n - 1):
			print 'c1:', _
			s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
		print(s)
			
A=Solution()
A.countAndSay(5)