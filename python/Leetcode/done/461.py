def hammingDistance(x, y):
	a=bin(x)[2:]
	b=bin(y)[2:]
	mm=int(max(len(a),len(b)))
	a=a.zfill(mm)
	b=b.zfill(mm)
	print a, b	
#	print temp
	diff=0
	for inta, intb in zip(a,b):
		if inta != intb:
			diff+=1
	print diff
	
hammingDistance(1,4)