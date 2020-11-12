def solution(S):
    # write your code in Python 2.7
	pair=["()", "[]", "()"]
	
	
	while S.find('()') >= 0 or S.find('[]') >= 0 or S.find('{}') >= 0:
			while S.find('()') >= 0:
				S=S.replace("()", "")
			while S.find('[]') >= 0:
				S=S.replace("[]", "")
			while S.find('{}') >= 0:
				S=S.replace("{}", "")
	print S
	if len(S) > 0:
		print 0
	else:
		print 1
		

	'''
	#corr:100 per:60 all:75
	while S.find('()') != -1 or S.find('[]') != -1 or S.find('{}') != -1:
		S=S.replace("()", "")
		S=S.replace("[]", "")
		S=S.replace("{}", "")
		
		#print '()', S.find('()') 
		#print '[]', S.find('[]') 
		#print '{}', S.find('{}') 
		
	if len(S) == 0 :
		print 1
		return 1
	else:
		print 0
		return 0
	'''
	'''
	# corr:66 perf:0
	for x in S:
		if x == '(':
			if temp[temp.index(x)+1] == ')':
				temp.remove(temp[temp.index(x)+1])
				temp.remove(x)
			else:
				print 0
				return 0

	for x in S:
		if x == '[':
			if temp[temp.index(x)+1] == ']':
				temp.remove(temp[temp.index(x)+1])
				temp.remove(x)
			else:
				print 0
				return 0
	for x in S:
		if x == '{':
			if temp[temp.index(x)+1] == '}':
				temp.remove(temp[temp.index(x)+1])
				temp.remove(x)
			else:
				print 0
				return 0
	if len(temp) == 0:
		print 1
		return 1
	else:
		print 0
		return 0
	'''
	'''		
	temp=[] # change signal to number
	rS=list(S)
	rS.reverse()
	for x in S:
		if x == '(':
			temp.append(1)
		if x == '{':
			temp.append(2)	
		if x == '[':
			temp.append(3)	
		if x == ')':
			temp.append(-1)
		if x == '}':
			temp.append(-2)	
		if x == ']':
			temp.append(-3)	
	print S
	temp2=temp[:]
	temp2.reverse()
	print temp
	print temp2
	ck=temp2.pop()
	print ck
	for x in temp:
		if len(temp2) >= 1:
			ck=temp2.pop()
		else:
			print 0
			return 0
		print 'x:', x
		print 'ck:', ck
		if x + ck == 0:
			temp
			return 1
	print 0
	return 0
	'''
	'''
	st=list(S)
	rst=st[:]
	rst.reverse()
	print 'st:' ,st
	print 'rst:' ,rst
	temp=rst.pop()
	for x in st:
		if len(rst) >= 1:
			temp=rst.pop()
		else:
			print 0
			return 0
			
		print 'x:', x
		print 'temp:', temp
		if x == temp:
			print 1
			return 1
	print 0
	return 0
'''	
print('=========')
solution('{[()()]}')
print('=========')
solution('([)()]')
print('=========')
solution(')(')
print('=========')
solution('({{({}[]{})}}[]{})')
