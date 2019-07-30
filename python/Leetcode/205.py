class Solution(object):
    def isIsomorphic(self, s, t):
		#print map(s.find, s) //get index for each element
		#print map(t.find, t)
		return map(s.find, s) == map(t.find, t)
		"""
		k=s
		j=t
		ls=list(set(s))
		lt=list(set(t))
		for x in set(s):
			if s.find(x) >= 0:
				k=k.replace(x, str(ls.index(x)))
			else:
				k=k.replace(x, 0)
			#print 'scon', k
		for y in set(t):
			if t.find(y) >= 0:
				j=j.replace(y, str(lt.index(y)))
				#print '1',j
			else:
				j=j.replace(y, 0)
			#print 'tcon', j
		
		print 'j:',j , 'k:', k
		if j==k:
			print True
		else:
			print False
	    """

A=Solution()
print('=1=')
A.isIsomorphic('title', 'peper')
print('=2=')
A.isIsomorphic('pig', 'tta')
