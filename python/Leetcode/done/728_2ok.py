class Solution(object):
    def selfDividingNumbers(self, left, right):
		ans=[]
		'''
		# Solutions by discussion
		def i(num):
			n = num
			while n:
				n, i = divmod(n, 10)
				if i == 0 or num % i != 0:
					return False
			return True

		retun filter(checkd, range(left , right+1))
		'''
		
		#Accept answer with low efficiency
		for x in range(left, right+1, 1):
			lenx = 0
			for y in list(str(x)):
				if int(y) != 0:
					if x % int(y) ==0:
						lenx+=1
				if lenx == len(str(x)):
					ans.append(x)
					
		print ans
					

	
A=Solution()
A.selfDividingNumbers(12,15)