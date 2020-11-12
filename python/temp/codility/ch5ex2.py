def solution(A):
	if A[0]==0:
		tal=1
	else:
		tal=0
	
	for x in A[1:]:
		#print 'x', x
		#print '11',A[x-1]
		#print 'tt', abs(x-A[A.index(x)-1])
		tal=tal+abs(x-A[A.index(x)-1])
		#print 'tal' , tal
	print tal

solution([0,1,0,1,1])
solution([0,1])
solution([0,7])