class Solution:
    def maxPower(self, s: str) -> int:
    	t=s[0]
    	#print(t)
    	temp=0
    	ms=0
    	#print(ms)
    	for x in s:
    		print(x)
    		if x == t:
    			temp+=1
    			print('1.', temp)
    		else:
    			if temp > ms:
    				ms=temp
    				print('2', ms)
    				temp=1
    				t = x	
    				print('3', temp, t)
    			else:
    				
    	print(ms)
    	return ms

A=Solution()
A.maxPower('hooraaaaaaaaaaay') 