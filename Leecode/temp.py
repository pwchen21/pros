def check(n):
	t = n	
	print 't:', t
	while n:
		print 'www'
		r = n
		print 'r:', r
		print 'n:', n
		if r == 0 or t%r != 0:
			 print False
		n = n/10
		print 'new n:', n
	print True
	
check(128)