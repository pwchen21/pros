def solution(N):
	x=1
	if x <= N:
		while x <= N:
			if (x % 3) == 0:
				if (x % 5) == 0:
					if (x % 7)== 0:
						print (str(x)+":FizzBuzzWoof")
					else:
						print (str(x)+":FizzBuzz")
				else:
					if (x % 7) == 0:
							print(str(x)+":FizzWooof")
					else:
						print(str(x)+":Fizz")	
			if ( x % 5) == 0 and (x % 3) != 0:
				if (x % 7) == 0:
					print(str(x)+":BuzzWoof")
				else:
					print(str(x)+":Buzz")
			if (x % 7) == 0 and not((x % 3) == 0 or (x % 5) == 0):
				print(str(x)+":Woof")
			
			if not (x % 3) ==0 and not (x % 5) == 0 and not(x % 7) ==0:
				print(x)
			x = x + 1
	pass
		
		
		
		
print("==1===")	
solution(105)
