import math
def constructRectangle(area):
	#square, and find the closest 2 numbers
	mid=int(math.sqrt(area))
	while mid > 0 :
		if area % mid ==0 :
			return(area/mid, mid)
		mid-=1
	'''right but the time execeed
	cb=[]
	res=[]
	len=1
	dis=area+1
	while len <= area:
		if area%len == 0:
			cb.append([len, area/len])
		len+=1
	print '1',cb
	for x in cb[:]:
		if x[0] < x[1]:
			cb.remove(x)
		else:
			if abs(x[1]-x[0]) < dis:
				res=x
				dis=x[1]-x[0]
				print res
	print 'res',res
	'''
constructRectangle(9999997)