class Solution(object):
    def selfDividingNumbers(self, left, right):
        
		ans=[]
		
		for x in xrange(left, right+1):
			false=0
			fac=list(str(x))
			print fac
			for i in fac:
				print 'x:', x
				print 'i:', int(i)
				if i == "0":
					false +=1
					print 'AA'
					break
				elif x % int(i) != 0:
					false +=1
			if false == 0:
				ans.append(x)
		print ans
	
	
A=Solution()
A.selfDividingNumbers(1,22)