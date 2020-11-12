def solution(A,B):
	BL=[]
	for x in B:
		BL.append(str(x))
	BLS =''.join(BL) 
	print type(BLS)
	print 'BLS', BLS
	print 'bls find:' , BLS.find('10')
	while BLS.find('10') != -1:
		print 'while'
		ind=0
		temp=str(B[0])
		for x in BL:
			print 'for'
			print 'temp:',temp , type(temp)
			print 'x:', x, type(x)
			if temp == '1' and x == '0':
				print 'ind', ind
				print A[ind],  A[ind+1]
				if A[ind] > A[ind+1]:
					print 'B', B
					print 'ind+1:', ind+1
					print 'B[ind+1]', B[ind+1]
					print 'temp', temp		
					#B.remove(B[ind+1])
					#B=B[:ind+1]+B[ind+2:]
					del B[ind+1]
					#A.remove(A[ind+1])
					#A=A[:ind+1]+A[ind+2:]
					del A[ind+1]
					print 'Ay',A
					print 'By',B 
					BLS=''.join(map(str, B))
					print 'bls1:', BLS
				else:
					print 'else1'
					#B.remove(B[ind])
					#B=B[:ind]+B[ind+1:]
					del B[ind]
					#A.remove(A[ind])					
					#A=A[:ind]+A[ind+1:]
					del A[ind]
					print 'Ax',A
					print 'Bx',B 
					BLS=''.join(map(str, B))
					print 'bls2:', BLS
			temp=x
			ind=+1
		#break;
	print 'Ao',A
	print 'Bo',B
	print len(B)


solution([2,3], [0,1])	
print 'expect 2'
print '======='	
solution([3,2], [0,1])	
print 'expect 2'
print '======='	
solution([2,3], [1,1])	
print 'expect 2'
print '======='
solution([2,3], [1,0])	
print 'expect 1'
print '======='
solution([3,2], [1,0])	
print 'expect 1'
print '======='
solution([4,3,2,1,5], [0,1,0,0,0])
print 'expect 2'