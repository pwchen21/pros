def fib(n, memo={}):
	if n < 2:
		print 'n<2 return:', 1
		return 1
	if n not in memo:
		#print "n, fib(n-1)", n, fib(n-1)
		print "n=", n
		print 'A:',fib(n-1)
		print 'B:',fib(n-2)
		re
		#memo[n]= fib(n-1) + fib(n-2)
		#print memo[n]
		#return memo[n]
	
fib(5)