def solution(N, A):
	
	counter=[0]*N
	last_max=0 #current number
	max_now=0  #
	print A
	
	for x in A:
		print 'x',x
		if x <= N:
			if counter[x-1] < last_max:
				counter[x-1] = last_max
			counter[x-1] +=1
			if counter[x-1] > max_now:
				max_now=counter[x-1]
		else:
			last_max=max_now
			print 'else'
		print counter
		print 'last_max:' , last_max , 'max_now',  max_now
	for i in xrange(len(counter)):
		if counter[i] < last_max:
			counter[i]=last_max
	print counter
	pass
	
	
	'''
	#4-corr:100 per:60
	counter=[0]*N
	last_max=0
	max_now=0
	for x in A:
		if x <= N:
			counter[x-1] +=1
			last_max=counter[x-1]
			if last_max > max_now:
				max_now=last_max
		else:
			counter=[max_now]*N
	print counter
	pass
	
	
	'''
	'''
	perfect soulution but not understand
    counters = [0]*N
    current_max = 0
    last_max = 0
    
    for el in A:
        if el < (N+1):
            if counters[el-1] < last_max:
                counters[el-1] = last_max
            counters[el-1] += 1
            if counters[el-1] > current_max:
                current_max = counters[el-1]
        else:
            last_max = current_max

    for i in xrange(len(counters)):
        if counters[i] < last_max:
            counters[i] = last_max
    return counters
	
	'''
	'''
	#2-complex no correct
	print 'A:', A
	setA=list(set(A))
	print 'set:', setA
	counter=[0]*N
	max_temp=0
	temp_list=[]
	if N <=0 or not A:
		return counter
	for x in setA:
		print 'x: ' , x, 'count:', A.count(x)
		for i in list(set(A[0:A.index(x)])):
			print 'i:', i 
			print 'A.index(x)', A.index(x)
			temp_list=A[0:A.index(x)]
			if temp_list.count(i) > max_temp:
				print 'A.count(i)', A.count(i)
				max_temp=temp_list.count(i)
				print 'max_temp', max_temp
				counter=[max_temp]*N
				print 'x>N' , counter
	for x in setA:
		if x <= N:
			print "x <= N"
			print 'x', x
			counter[x-1]=counter[x-1]+A.count(x)
			
		print counter
	'''
	'''
	#3-correct:100 perf.:40 simple
	counter=[0]*N
	if N <=0 or not A:
		return counter
	for x in A:
		if x <= N:
			counter[x-1] +=1
		else:
			counter=[max(counter)]*N			
		print counter
	return counter
	
	'''
	'''
	#4-	correct:100 perf.:40
	#set counter
	counter=[]
	if N <=0 or not A:
		#print 'N<=0'
		print counter
		return counter
	for x in range(N):
		counter.append(0)
	
	for x in A:
		if x > N:
			#print 'x>=N', 'x:', x 
			max_N=max(counter)
			#print 'max_N: ', max_N
			for y in range(N):
				#print 'A[y]: ',A[y]
				counter[y]=max_N
		if x <= N:
			#print 'x<N', 'x:', x 
			counter[x-1]=counter[x-1]+1
		print counter
	return counter
	'''		
		
'''
print 'prob1==='
solution(5,[1,2,4,5,6])
print 'prob2==='
solution(5,[1,2,4,3,6,4,5,6])
print 'prob3==='
solution(0,[1,2,4,5,5])
print 'prob4==='
solution(5,[])
'''
print 'prob5==Sample='
solution(2,[1,1,1, 1, 2,1,3])