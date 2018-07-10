class Solution(object):
    def reverse(self, x):
		ax=abs(x)
		strx=str(ax)
		lsx=list(strx)
		lsx.reverse()
		ri=int(''.join(lsx))
		if x > 0x7FFFFFFF or x < -0x7FFFFFFF:
			return 0
		elif x < 0:
			return -ri
		else:
			return ri


	
sol=Solution()
sol.reverse(1233333333333333333333333)
