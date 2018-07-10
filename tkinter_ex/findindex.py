A=[1, 2, 3, 4, 5, 6, 7, 3, 2, 1, 2, 4, 6]
temp=0

while temp != 'N':
	try:
		temp=A.index(2,temp+1)
		print('temp:', temp)
		print(temp)
	except ValueError:
		temp='N'