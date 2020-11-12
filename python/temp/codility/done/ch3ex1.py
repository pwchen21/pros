# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
	print("len:"+str(len(A)))
	sum_w=((1+(len(A)+1))*(len(A)+1))/2
	print("w:"+str(sum_w))
	sum_r=sum(A)
	print("r:"+str(sum_r))
	return(sum_w-sum_r)
	'''if not A:
		return('1')
	#print("list:"+str(len(A)))
	i=1
	B=[]
	while i < len(A)+1:
		B.append(i)
		i=i+1
	#	print(B)
	for x in A:
	#	print("x:"+str(x))
		if x in B:
			B.remove(x)
	#		print(B)
	return(B.pop())
	'''
	pass
	
solution([2,3,1,5])