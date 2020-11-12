#coding:utf-8

def solution(A):
    # write your code in Python 2.7
	minspace=sum(A)
	x=0
	left=sum(A[0:x]))
	right=sum(A[x:])
	print(left)
	print(right)
	'''
	while x < len(A):
		if (left - right) < minspace:
			minspace=left-right
		print("min:"+ str(minspace))
		x=x+1
	'''
	return minspace