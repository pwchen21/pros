class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
			print "[1]"
			#return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
				print "[2]"
				print strs[0][:i]
				#return strs[0][:i]
        else:
			print "[3]"
			print min(strs)			
            #return min(strs)
			
A=Solution()
A.longestCommonPrefix(['abc', 'abd', 'abf'])