def addDigits(num):
	listnum=list(str(num))
	while len(listnum) !=1:
		total = 0
		for x in listnum:
			total=total+int(x)
		listnum=list(str(total))
	print total
	
addDigits(38)

