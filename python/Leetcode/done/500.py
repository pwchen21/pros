#def findWords(words):
def findWords(words):
	L1="qwertyuiopQWERTYUIOP"
	L2="asdfghjklASDFGHJKL"
	L3="zxcvbnmZXCVBNM"
	group=''
	for x in words[:]:
		temp=0
		wd=list(x)		
		if L1.find(wd[0]) >= 0:
			group=L1			
		if L2.find(wd[0]) >= 0:
			group=L2
		if L3.find(wd[0]) >= 0:
			group=L3
		if len(x) > 1:
			for y in wd[1:]:
				if y not in group:
					temp = 1
					break
			if temp == 1:
				words.remove(x)
	print words

	'''
	L1="qwertyuiopQWERTYUIOP"
	L2="asdfghjklASDFGHJKL"
	L3="zxcvbnmZXCVBNM"
	#group=[L1,L2,L3]
	#Li1=list(L1)
	#Li2=list(L2)
	#Li3=list(L2)
	group=''
	result=[]
	for x in words[:]:
		print "========"
		temp=0
		print x
		wd=list(x)		
		print 'wd:', wd
		print 'wd0:',wd[0]
		if L1.find(wd[0]) >= 0:
			group=L1			
		if L2.find(wd[0]) >= 0:
			group=L2
		if L3.find(wd[0]) >= 0:
			group=L3
		print group
		
		if len(x) > 1:
			for y in wd[1:]:
				#print 'y',y
				#print 'group', group
				#print group.find(y)
				#print y in group
				if y not in group:
					print 'hh'
					temp = 1
					break
			if temp == 1:
				words.remove(x)
			
		print words
		
		#	if y not in group:
		#		words.remove(wd)
		#		break
		#result.append(x)
		#print 'words',words
		'''
findWords(["hello", "Alaska", "Dad", "Peace"])
findWords(["abdfs","cccd","a","qwwewm"])
#

