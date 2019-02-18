def rank(st, we, n):
	if len(st)==0:
		print("No participants")
		return "No participants"

	#print(st,we,n)
	st=st.split(',')
	wt={}
	#print('ls', len(st))	

	if n > len(st):
		print("Not enough participants")
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
	print(srh(ks, wt))
	return(srh(ks, wt))
	#print(wt[a[n-1]])
	#return wt[a[n-1]]
		
def getn(name):
	sum=0
	#print('p2:' ,name)
	for y in name:
		#print('y:', y)
		#print('ord:', ord(y.lower())-96)
		sum += (ord(y.lower(()) - 96)
	#print('sum:', sum)
	return sum
	

def srh(ks,wt):
	#print('srh:' ,  wt)
	srhl=[]
	j=0
	rs=""
	for x in wt:
		if wt[x] == ks:
			#print(x)
			srhl.append(x)
	for y in srhl:
		#print('y', y)
		#print('y1', y[0])
		#print('g', getn(y[0].lower()))
		if getn(y[0].lower()) > j:
			#print('hh')
			j=getn(y[0])
			rs=y
	#print('x:', rs)
	return(rs)	
	#return srhl.sort()[0]
			
print("==1==")	
rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)
	
print("==2==")
rank("Lagon,Lily", [1, 5], 2)

print("==3==")
rank("", [4, 2, 1, 4, 3, 1, 2], 6)

print("==4==")
rank("Bmn,Ann", [2,2], 1)


print("==5==")
rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden",[1, 3, 5, 5, 3, 6],2)
