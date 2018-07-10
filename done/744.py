class Solution(object):
    def nextGreatestLetter(self, letters, target):
		sl=sorted(list(set(letters)))
		#print sl
		to=ord(target)
		if ord(sl[-1]) < to:
			return sl[0]
			#print '1'
		else:
			for x in sl:
				if ord(x) > to:
					return x
					#print '2'
				if ord(x) == to:
					if sl.index(x) == len(sl)-1:
						return sl[0]
						#print '3'
					else:
						return sl[sl.index(x)+1]
						#print '4'
				
	
A=Solution()

A.nextGreatestLetter(["d", "g", "i"], "i")