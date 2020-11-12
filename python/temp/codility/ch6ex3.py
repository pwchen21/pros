import itertools
def solution(A):
    # write your code in Python 2.7
	A=sorted(A,reverse=True)
	print A
	a=b=c=0
	for x in A:
		a,b,c=x,a,b
		print a,b,c
		if a+b>c and b+c>a and c+a>b:
			print 'yes!'
	print 0
	''' corr 100 perf 33 sc 75
	count=0
	for x in itertools.combinations(A,3):
		comb=list(x)
		if (comb[0] + comb[1] > comb[2]) and  (comb[1] + comb[2] > comb[0]) and  (comb[2] + comb[0] > comb[1]):
			count = 1
			break
	print count
	'''
	''' 
	#corr60 perf0 sc37
	count = 0
	temp = []#save the set
	for x in itertools.combinations(A,3):
		comb=list(x)
		print comb
		if (comb[0] + comb[1] > comb[2]) and  (comb[1] + comb[2] > comb[0]) and  (comb[2] + comb[0] > comb[1]) and (len(set(comb)) != 1):
			temp.append(x)
			count +=1
			print '+1'
	temp=set(temp)
	print 'here', temp
	print len(temp)
	'''

	
solution([7,6,6,6,6,5,2,6,1,2,4])