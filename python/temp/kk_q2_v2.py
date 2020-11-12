def solution(N):
	op=[]
	x = 1
	while x <= N:
		if x % 3 == 0:
			op.append("Fizz")
		if x % 5 == 0:
			op.append("Buzz")
		if x % 7 == 0:
			op.append("Woof")
		if not op:
			pass
		else:
			print (''.join(op)), "ttt"
		if not(( x % 3) ==0 or (x % 5) ==0 or (x % 7) ==0):
			print x
		x += 1
		op = []
	pass
	
solution(19)