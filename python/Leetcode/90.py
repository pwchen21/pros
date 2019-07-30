class Solution(object):
	def subsetsWithDup(self, S):
		res = [[]]
		S.sort()
		for i in range(len(S)):
			if i == 0 or S[i] != S[i - 1]:
				print 'S[i]' , S[i]
				print 'S[i-1]', S[i-1]
				l = len(res)
				print "len:", l
			for j in range(len(res) - l, len(res)):
				print S[i]
				res.append(res[j] + [S[i]]) # MAKE A CHANGE HERE : res[j].append(S[i]);res.append(res[j])
		print res
		
A=Solution()
A.subsetsWithDup([1,2,2])