class Solution:
    def shortestToChar(self, s: str, c: str):
    	ans=[]
    	ci=-1
    	for x in range(len(s)):
    		print('===s[x]:', s[x])
    		print('c:', c)
    		if s[x] == c:
    			print('chk1')
    			ans.append(0)
    			ci=x
    		else:
    			print('chk2')
    			s1=s[x+1:]
    			print('s1: ', s1)
    			if ci != -1 :
    				t1=(x-ci-1)
    				print('chk3', t1)
    			else:
    				print('chk4')
    				t1=10001

    			if c in s1:
    				t2=(s1.index(c))
    				print('chk5', t2)
    			else:
    				print('chk6')
    				t2=10001

    			ans.append(min(t1,t2)+1)
    			print(ans)
    	print('final result:', ans)

'''
		#Accepted answer
    	ans=[]
    	ci=0
    	for x in range(len(s)):
    		print('===s[x]:', s[x])
    		print('c:', c)
    		if s[x] == c:
    			print('chk1')
    			ans.append(0)
    			ci=x
    		else:
    			print('chk2')
    			s1=s[:x+1]
    			s2=s[x+1:]
    			print('s1: ', s1)
    			print('s2: ', s2)
    			if c in s1:
    				t1=(x-ci-1)
    				print('chk3', t1)
    			else:
    				print('chk4')
    				t1=10001

    			if c in s2:
    				t2=(s2.index(c))
    				print('chk5', t2)
    			else:
    				print('chk6')
    				t2=10001

    			ans.append(min(t1,t2)+1)
    			print(ans)
    	print('final result:', ans)
'''

A=Solution()
A.shortestToChar('baaaa', 'b')
        