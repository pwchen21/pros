def isAnagram(s, t):
	tl=list(t)
	tl.reverse()
	
	if s == ''.join(tl):
		return True
	else:
		return False

isAnagram('ab' , 'a')  