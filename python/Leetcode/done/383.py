class Solution(object):
    def canConstruct(self, ransomNote, magazine):
		mag=list(magazine)
		for x in ransomNote:
			print 'x:', x
			if x in mag:
				mag.remove(x)
				print 'mag', mag
			else:
				print 0
				return 0
		print 1
		return 1
		"""
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
A=Solution()
A.canConstruct('aa', 'acba')
