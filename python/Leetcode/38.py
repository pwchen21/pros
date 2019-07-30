class Solution:
	def countAndSay(self, n):
		if n == 1:
			print(1)
       #print(n)
		al=[]
		ln=list(str(n))
		#print("lenN", len(n))
		t='t'
		for x in range(len(str(n))):
			#print('x',x)
			cn=1
			#print('j', ln[x])
			if ln[x] !=t:
				if x != len(str(n))-1:
					while ln[x] == ln[x+1]:					
						x=x+1
						cn+=1
						#print('x,cn', x, cn)
						
					al.append(cn)
					al.append(ln[x])
				else:	
					al.append(cn)
					al.append(int(ln[x]))
			
			t=ln[x]
			#print('t',t)
		print(''.join(str(m) for m in al))
			
A=Solution()
A.countAndSay(1)