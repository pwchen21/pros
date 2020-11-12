
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
def solution(A):
	A=sorted(A)
	print(A)
	x=0
	if len(A)==1:
		print A[0]
	else:
		for x in range(0,len(A),2):
			if x+1 == len(A):
				return(A[x])
			if A[x] != A[x+1]:
				return A[x]
			
	'''
	def solution(A):
	if len(A) == 1:
		return A[0]
	A=sorted(A)
	#print(A)
	
	#print range(0,len(A),2)
	for i in range(0,len(A),2):
		#print("i:" + str(i))
		#print("len:" + str(len(A)))
		if i+1 == len(A):
			#print("00")
			return A[i]
		if A[i] != A[i+1]:
			#print("11")
			return A[i]
	'''
	'''v=A[0]
	nl=[]
	if len(A)>0
		for x in A:
			if x != v:
				nl.append(x)
				x += 1
		if v in A:
			#print(nl)
			#test=len(nl)
			#print("len:"+ str(test))
			print(nl[len(nl)-1])
	else:
		return(A[0])
    '''
	'''def solution(A):
	v=A[0]
	nl=[]
	if len(A)>1 and type(A) is list:
		for x in A:
			if x != v:
				nl.append(x)
				x += 1
		if v in A:
			#print(nl)
			#test=len(nl)
			#print("len:"+ str(test))
			return(nl[len(nl)-1])
	else:
		return(A[0])
		'''
print("problem1")
solution([2, 2, 3, 3, 4])
print("problem2")
solution([42])