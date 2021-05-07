class Solution:
    def minRemoveToMakeValid(self, s):
    	sl=list(s)
    	temp=[]
    	for x in range(len(s)):
    		#print(s[x])
    		if not s[x].isalpha():
    			if s[x] == '(':
    				temp.append([x, s[x]])
    			else:
    				if temp and temp[-1][1] == '(':
    					temp.pop()
    				else:
    					temp.append([x, s[x]])
    	
    	print('sl', sl)
    	print('temp', temp)

    	for x in temp[-1::-1]:
    		#print(x)
    		del sl[x[0]]
    		#s.remove(s[12])
    		#print('sl', sl)   		
    		#print(sl)
    	print(''.join(sl))

A=Solution()
# A.minRemoveToMakeValid('lee(t(c)o)de)')
# print('=======')
# A.minRemoveToMakeValid('le(a))((b)')
# print('=======')
A.minRemoveToMakeValid('))((')
        