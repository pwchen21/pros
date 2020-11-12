def solution(A):
	#100 answer
	A=list(set(A))
	A=sorted(A)
	for x in A[:]:
		if x > 0:
			break
		else:
			A.remove(x)
	if not A:
		return 1

	temp=1
	for x in A:
		if x !=temp:
			return temp
		temp+=1
	
	if A[-1] == max(A):
		return max(A)+1
'''
	A=list(set(A))
	A=sorted(A)
	print A
	for x in A[:]:
		print("x:" + str(x))
		if x <= 0:
			A.remove(x)

		else:
			break

	if not A:
		print 1
		return 1
	temp=1
	print A
	for x in A:
		if x !=temp:
			print temp
			return temp
		temp+=1
	
	if A[-1] == max(A):
		print(max(A)+1)
		return max(A)+1
'''
	'''
	if min(A) <= 0:
		temp=min(A)
	else:
		temp=1
	for x in A:
		if x != temp:
			if temp <= 0:
				print 1
				return 1
			else:
				print temp
				return temp
		temp+=1
	if A[-1] == max(A):
		#print ('A[-1]:' +str(A[-1]))
		#print ('max(A):' +str(max(A)))
		if max(A) <= 0:
			print 1
			return 1
		if max(A) > 0:
			print(max(A)+1)
			return max(A)+1
	'''

#solution([1,3,4,5,7])
#solution([2,3,9,6,1])				
#solution([])				
#solution([101,102,103])			
#solution([2])	
#solution([-1,3,5,7,9])		
#solution([1])	
#solution([-3,-2,2,3,4,4,5])	
#solution([-1])	
#solution([77,0,87, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 13, 18, 19,99 , 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 1,88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111])
solution([0, 1, 2, -3, 4,-9, 6, -7, -16,3])