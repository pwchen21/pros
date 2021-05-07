class Solution:
	def scoreOfParentheses(self, s):
		print(s)
		x=s.replace(')(', ')+(')
		print(x)
		x=x.replace('()', '1')
		print(x)
		x=x.replace(')', ')*2')
		print(eval(x))
		return eval(x)

A=Solution()
A.scoreOfParentheses('(()(()))')