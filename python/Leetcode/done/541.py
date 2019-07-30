def reverseStr(s, k):
	temp=[]
	tstr=[]
	sl=list(s)
	print sl
	st=0
	k2=k
	rou=len(s) % k
	rs=0
	while k2 <= len(sl):
		print k, st, len(sl)
		cbo=sl[st:k2]
		rsl=list(cbo)
		if rs % 2 == 0:
			rsl.reverse()
			temp.append(rsl)
		else:
			temp.append(cbo)
		st=k2
		k2=k2+k
		rs+=1
		print 'k2', k2
		print temp
		print 'rs:', rs
	
	if rou != 0:
		print 'here RS:', rs
		if rs == 0 :
			print '##'
			last=sl[::-1]
		else:
			if rs % 2 == 0:
				last=sl[-rou:]
				last.reverse()
				print('--', -rou)
			else:			
				last=sl[k2-k:]
				print('**', k2-k)
	
		temp.append(last)		
		print temp
		
	for x in temp:
		tstr.append(''.join(x))
	
	print ''.join(tstr)






reverseStr('abcdefg',8)
print '==='
reverseStr('hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl',39)