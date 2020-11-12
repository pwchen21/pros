def solution(X, A):
	cl=set()
	for x in range(0,len(A)):
		cl.add(A[x])
		if len(cl) == X:
			return x
	return -1
	
	'''complex to high
	print(X,A)
	cl=range(1,X+1)
	print 'cl:', cl
	for x in A:
		if x in cl:
			cl.remove(x)
			print cl
			if not cl:
				print A.index(x)
				return A.index(x)
	print 'result:' +str(-1)
	return -1
	'''
				
	'''
	ls=[]
	ls=sorted(A)
	ls=list(set(ls))
	print(ls)
	temp=1
	for x in ls:
		print 'temp:' + str(temp)
		print 'x:' + str(x)
		if x == temp:
			if x == X:
				print 'result:' + str(A.index(x))
				return A.index(x)
				#break
			else:
				if temp == len(ls):
					print 'result:' + str(-1)
					return -1
				temp += 1
		else:
			print 'result:' + str(-1)
			return -1
	'''
	'''
	print "X:" + str(X)
	for fstep in A:
		if fstep >= X:
			print 'Result:' + str(A.index(fstep))
			break
			#return A.index(fstep)
		else:
			print -1
			return -1
	'''		
print '==pro1=='
solution(5,[3])
print '==pro2=='
solution(5,[7])
print '==pro3=='
solution(5,[1,3,1,4,2,3,5,4])
print '==pro4=='
solution(2,[1,1,1,1])
print '==pro5=='
solution(3, [1, 3, 1, 3, 2, 1, 3])