def fizzBuzz(self, n):
	op=[]
	result=[]
	x = 1
	while x <= n:
		if x % 3 == 0:
			op.append("Fizz")
		if x % 5 == 0:
			op.append("Buzz")
		if not op:
			pass
		else:
			result.append(''.join(op))
			#print (''.join(op)), "ttt"
		if not(( x % 3) ==0 or (x % 5) ==0):
			result.append(str(x))
		x += 1
		op = []
	return result
	
solution(19)