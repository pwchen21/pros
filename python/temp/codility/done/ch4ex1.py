def solution(A):
#100
	if not A:
		return 0
	A=sorted(A)
	temp=1
	for x in A:
		if x != temp:
		    return 0
		temp +=1
	if temp-1 == max(A):
	    return 1
'''

	def solution(A):
	if not A:
		return 0
	A=sorted(A)
	temp=1
	for x in A:
		if x != temp:
		    return 0
		temp +=1
	if temp-1 == max(A):
	    return 1
	pass
'''
'''
	if not A:
		print 0
		return 0
	A=sorted(A)
	print(A)
	temp=1
	for x in A:
		if x == temp:
		    if temp == max(A):
				print 1
				return 1
		else:
			print 0
			return 0
		temp +=1
	print(temp)
	pass
'''
'''
	# write your code in Python 2.7
	print(A)
	print("sum:"+str(sum(A)))
	if len(A) = 0:
		print 0
		return 0
	if len(A) = 1:
		print 1
		return 1
	tempSum=min(A)
	print("original tempSum:" + str(tempSum))
	for x in range(min(A)+1,max(A)+1,1):
		tempSum +=x
		print("tempSum:" + str(tempSum))
	if sum(A) == tempSum:
		print 1
		return 1
	else:
		print 0
		return 0
    ============
	if len(A) <=2:
		print 0
		return 0
	
	A=sorted(A)
	print(A)
	temp=min(A)
	for x in A:
		if x == temp:
		    if temp == max(A):
				print 1
				return 1
		else:
			print 0
			return 0
		temp +=1
	print(temp)
	'''	

print("problem1====")
solution([4,1,3,2])
print("problem2:===")
solution([4,1,2])
print("problem3:===")
solution([])
print("problem4:===")
solution([4])
print("problem5:===")
solution([5,9,7,8])
print("problem6:===")
solution([100,99,102,101])

