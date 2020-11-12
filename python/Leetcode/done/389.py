def fn(s,t):

	for x in t:
		#print x
		#print t.count(x)
		#print s.count(x)
		if t.count(x) != s.count(x):
			print x
print "=="
fn("abc","abdc")
print "=="
fn("a","aa")