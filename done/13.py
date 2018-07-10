class Solution:

	def romanToInt(self, s):
		ne=0
		po=0
		ro = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
		for x in range(0,len(s)-1):
			print s[x],':', ro[s[x]] 
			if ro[s[x]] < ro[s[x+1]]:
				ne+=ro[s[x]]
				print '1-ne:', ne
			else:
				po+=ro[s[x]]
				print '2-po:', po
		print po , ne , ro[s[-1]]
		print po - ne + ro[s[-1]]
		
		
        ''' great solution 	
		roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
		z=0
		for i in range(0, len(s) - 1):
			print s[i]
			if roman[s[i]] < roman[s[i+1]]:
				z -= roman[s[i]]
				print 'z-:', z
			else:				
				z += roman[s[i]]
				print 'z+:', z
		print z + roman[s[-1]]
        '''
test=Solution()
test.romanToInt('MCMXCVI')