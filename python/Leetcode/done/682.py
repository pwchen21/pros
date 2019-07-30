class Solution(object):
    def calPoints(self, ops):
		score=[]
		for x in ops:
			if x == 'C':
				score.pop()
			elif x == 'D':
				score.append(score[-1]*2)
				#print '1', type(score.append(score[-1]*2))
			elif x == '+':
				score.append(score[-1]+score[-2])
			else:
				score.append(int(x))
		#print score
		print sum(score)
		
A=Solution()
A.calPoints(["5","-2","4","C","D","9","+","+"])