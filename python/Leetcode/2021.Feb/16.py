class Solution:
	def letterCasePermutation(self, S):
		#Solution2
		ans=[]
		temp=[]
		if S.isdigit():
			return([S])

		if S[0].isalpha():
			temp.append(S[0].lower())
			temp.append(S[0].upper())
		else:
			temp.append(S[0])
		
		for x in S[1:]:            
			if x.isalpha():
				for y in temp:
					ans.append(y+x.lower())
					ans.append(y+x.upper())
			else:
				for y in temp:
					ans.append(y+x)			
			temp=ans
			ans=[]
		print(temp)
		return(temp)
		'''
		#Solution 1
		ans=[]
		temp=[]
		if S.isdigit():
			print('1')
			print([S])
			return([S])
		for x in S:
			print('2', x)
			print('2t', temp)
			if x.isalpha():
				if not temp:
					ans.append(x.lower())
					ans.append(x.upper())
				else:
					for y in temp:
						ans.append(y+x.lower())
						ans.append(y+x.upper())
						print(ans)
			else:
				for y in temp:
					ans.append(y+x)
			
			temp=ans
			ans=[]
		print(temp)
		'''

A=Solution()
A.letterCasePermutation('ab1c')
print('================')
A.letterCasePermutation('0')