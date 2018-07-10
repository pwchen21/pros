class Solution(object):
	def judgeCircle(self, moves):
		print moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")
		
A=Solution()
A.judgeCircle("LR")