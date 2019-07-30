import math
class Solution(object):
    def countPrimeSetBits(self, L, R):
		ans=[]
		for x in range(L, R+1):
			print "x:", x
			
			pc=bin(x)[2:].count('1')			
			print "  pc:", pc
			spc=int(math.sqrt(pc))+1
			if pc > 1:
				for y in range(2, spc):
					print "   y:", y
					if pc % y == 0:
						break
				else:
					print "else here!!"
					ans.append(x)
		print ans
		print len(ans)

A=Solution()
A.countPrimeSetBits(842,888)