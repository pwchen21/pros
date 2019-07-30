

def rank(st, we, n):
	if len(st)==0:
		#print("No participants")
		return "No participants"

	print(st,we,n)
	st=st.split(',')
	wt={}
	#print('ls', len(st))	

	if n > len(st):
		#print("Not enough participants")
		return "Not enough participants"

		
	for x in st:
		#print('p1:',x)
		#l=x.lower()
		#print('l:', l)
		wt[x] = (len(x) + getn(x)) * we[st.index(x)]
		#print(wt)
	#print("a:", [ v for v in sorted(wt.keys())])
	#print("b:", n)
	ks=sorted(wt.values(), reverse=True)[n-1]
	#print(sorted(wt.values(), reverse=True))
	#print(ks)
	#print("wt.keys()", wt.values())
	#print(list(wt.values())[n-1])
	#print(list(A.keys())[list(A.values()).index(2)])
	#a=[ v for v in sorted(wt.keys())]
	#a.sort(reverse=True)
	#print(srh(ks, wt))
	return(srh(ks, wt))
	#print(wt[a[n-1]])
	#return wt[a[n-1]]
		
def getn(name):
	sum=0
	#print('p2:' ,name)
	for y in name:
		#print('y:', y)
		#print('ord:', ord(y.lower()))
		sum += ord(y.lower()) - 96
	print('sum:', sum)
	return sum

def srh(ks,wt):
	print('srh:' ,  wt)
	srhl=[]


	for x in wt:
		if wt[x] == ks:
			#print(x)
			srhl.append(x)
	srhl.sort()
	print(srhl, srhl[0])
	return(srhl[0])	













