class Solution(object):
    def lengthOfLongestSubstring(self, s):
		leng=0
		maz=0
		temp=[]
		for x in s:
			if x not in temp:
				print '--'
				print 'x:', x
				temp.append(x)
				print temp
				leng+=1
				if len(temp) > maz:
					maz=len(temp)
			else:
				#print len(temp)
				temp=[]
				leng=1
				temp.append(x)
		
		return maz

		
A=Solution()
print "=="
A.lengthOfLongestSubstring('abcabcbb')

'''
print "=="
A.lengthOfLongestSubstring('bbbbb')
print "=="
A.lengthOfLongestSubstring('pwwkew')
print "=="
A.lengthOfLongestSubstring('c')
print "=="
A.lengthOfLongestSubstring('dvdf')
'''