class Solution:
    def isValid(self, s):
    	tl=[]
    	for x in s:
    		if x in ['{','[', '(']:
    			tl.append(x)
    		else:
    			#print('			', x, tl[-1])
    			if not tl:
    				print('no')
    				return False
    			elif (x == ')') & (tl[-1] == '('):
    				tl.pop()
    			elif (x == ']') & (tl[-1] == '['):
    				tl.pop()
    			elif (x == '}') & (tl[-1] == '{'):
    				tl.pop()
    			else:
    				print('no')
    				return False

    	print (tl==[], 'Last')
    	return (tl==[])



A=Solution()
print(A.isValid('{[()]}'), 1)
print(A.isValid('{[(])}'), 0)
print(A.isValid('{[()()]}'), 1)
print(A.isValid('({})'), 1)
print(A.isValid('()()((}))'),0)
print(A.isValid('['), 0)
print(A.isValid('(){}}{'), 0)
print(A.isValid(''), 0)

