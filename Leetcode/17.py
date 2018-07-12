class Solution(object):
    def letterCombinations(self, digits):
		pd={2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
		set=[]
		ld=list(digits)
		ild=[]
		for x in ld:
			ild.append(int(x))
		#print ild		
		#print pd[ild[0]]
		#for x in pd[ld]
		
Ans=Solution()
Ans.letterCombinations("23")