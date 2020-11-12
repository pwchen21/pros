def solution(A,B,K):
	
	print B/K - A/K +int(A%K==0)
#    total. 25 cor.25 perf.25
'''
	count = 0 
	if A < K:
		n=1
	else:
		n = A / K
	while K*n <= B:
		print 'test', K*n
		count +=1
		n += 1
	print count
'''
#    total. 50 cor.100 perf.0
'''
	count=0
	for x in range(A, B+1):
		if x % K == 0 :
			count+=1
	print count
'''

	
solution(11,345,17)
solution(6,11,2)
#solution(9,7,0)
solution(10,10,5)
solution(0,0,11)
solution(0,20,11)