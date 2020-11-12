def solution(X, Y, D):
    # write your code in Python 2.7
	
	if ((Y-X)%D) == 0:
		return ((Y-X) / D)
	else:
		return ((Y-X) / D + 1)
	
	'''
	複雜度太高
	while Y > X :
		print(X, Y, D)
		X += D
		times += 1
	return(times)
	'''
	pass
	
solution(10,85,30)