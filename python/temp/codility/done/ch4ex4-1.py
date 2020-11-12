def solution(N, A):
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
	
solution(5,[3,4,4,6,1,4,4])