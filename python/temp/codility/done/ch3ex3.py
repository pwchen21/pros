
def solution(A):
    # write your code in Python 2.7
	B=[]
	sumA=sum(A)
	print("sumA:" + str(sumA))
	Left=0
	Right=0
	if len(A) < 1:
		return 0
	for x in A[0:len(A)-1]:
		Left=Left+x
		Right=sumA-Left
		print("left:" + str(Left) + " right:" +str(Right))
		B.append(abs(Right-Left))
		print(B)
	print min(B)
	'''
	x=1
	B=[]
	if len(A) < 1:
		return 0
	while x < len(A):
		#print("x:" +str(x))
		#print(len(A))
		#print("len:" +str(len(A)))
		left=sum(A[0:x])
		right=sum(A[x:])
		#print("left:" + str(left) + " right:" +str(right))
		B.append(abs(left-right))
		x=x+1
	return min(B)
	'''

print("=====Q1======")
solution([3,1,2,4,3])
print("=====Q2======")
solution([-1000,1000])
print("=====Q3======")
solution([1000,-1000])