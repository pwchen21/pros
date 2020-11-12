def findComplement(num):
	boo=bin(num)[2:]
	boo= map(int, boo)  #change all str to int in list
	op=[1]*len(boo)
	#op=map(str, op)
	#opn=int(''.join(op))
	#boo=int(boo)
	
	#print type(boo), type(opn)
	#print boo
	#print op
	#result= boo ^ opn

	temp =[]
	for xa, xb in zip(boo,op):
		temp.append(xa ^ xb)
	temp=map(str, temp)
	#print temp
	tempj=''.join(temp)
	#print tempj
	result=int(tempj, 2)
	print result
	 
	
findComplement(1983)
findComplement(5)
findComplement(2)
