class Solution(object):
    #Exceed Memory
	def findIntegers(self, num):
		count=0
		if num >=1:
			count=2
		for x in range(2, num+1, 1):
			if bin(x)[2:].find('11') == -1:
				count+=1
		print count
	'''
	def findIntegers(self, num):
		temp=[] #Binary to list
		cons=[]
		for x in range(2, num+1, 1):
			binX=bin(x)[2:]
			#print 'x:', x ,'binx:',  binX
			#print 'bindx:', binX.find('11')
			#print 'bindx:', binX.find('00')
			# Check if consective 
			if binX.find('11') == -1:
				cons.append(x)
		if num >=1:
			cons.append(0)
			cons.append(1)
		#print cons
		print 'answer', len(cons)	
	'''	
A=Solution()
A.findIntegers(20)
print '==='
A.findIntegers(10000000)