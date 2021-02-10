def reverse(x):
	temp=str(abs(x))
	temp=int(temp[::-1])
	#print(temp)
	if (temp > 2147483647):
		print(0)
		return 0
	elif x < 0 :
		print(-temp)
		return(-temp)
	else:
		print(temp)
		return(temp)

reverse(-201)
reverse(10030)
reverse(-5010)
reverse(-201)