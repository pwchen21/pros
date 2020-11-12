def detectCapitalUse(word):
	if word.isupper() == True or word.islower() == True:
		return True
	if word[0].isupper() == True & word[1:].islower() == True:
		return True
	return False

	
print "=="
detectCapitalUse("USA")
print "=="
detectCapitalUse("Capital")
print "=="
detectCapitalUse("abc")
print "=="
detectCapitalUse("FLag")