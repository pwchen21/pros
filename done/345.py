import re

class Solution(object):
    def reverseVowels(self, s):
		rs=[]
		rs=re.findall('(?i)[aeiou]', s)
		print rs
		def lbd(m):
			return rs.pop()			
		print re.sub('(?i)[aeiou]', lbd ,s)

			
A=Solution()
A.reverseVowels("hello")