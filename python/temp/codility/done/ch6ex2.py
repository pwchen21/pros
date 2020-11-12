def solution(A):
    # write your code in Python 2.7
	#corr/pef=100 by myself
	sortA=sorted(A , reverse=True)
	max1=sortA[0] * sortA[1] * sortA[2]
	max2=sortA[0] * sortA[-1] * sortA[-2]
	print max(max1, max2)
	
	#corr/pef=100 by myself
	'''
	sortA=sorted(A , reverse=True)
	Po=[]
	Ne=[]
	for x in A:
		if x > 0:
			Po.append(1)
		else:
			Ne.append(1)
	if len(Po) == 0:
		return sortA[0] * sortA[1] * sortA[2]
	if len(Po) == 1 or len(Po) == 2:
		return sortA[0] * sortA[-1] * sortA[-2]
	if len(Po) >=3:
		if len(Ne) >= 2:
			if sortA[-1]*sortA[-2] > sortA[1] * sortA[2]:
				return sortA[0]*sortA[-1]*sortA[-2]
			else:
				return sortA[0] * sortA[1] * sortA[2]
		else:
			return sortA[0] * sortA[1] * sortA[2]
	'''
	'''
	#corr=50 per=40
    B=sorted(A, reverse = True)
    return B[0]*B[1]*B[2]
	'''

solution([-3, 1, 2, -2, 5, 6])	
solution([-4, -6, 3, 4, 5])