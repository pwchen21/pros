class Solution:
    def isPalindrome(self, s: str) -> bool:
    	#print(len(s))
    	A=int(len(s)/2)
    	n=1
    	#print(A)
    	for x in s[:]:
    		#print(x, 'is alpha ', x.isalnum())
    		if x.isalnum() == True:
    			t=s[-n]
    			while t.isalnum() != True:
    				n+=1
    				t=s[-n]
    			#print('compare:', t)
    			print('1:', x.lower() , ' 2:', t.lower())
    			if x.lower() != t.lower():
    				print(False)
    				return False
    			else:
    				n+=1
    	print (True)
    	return True


A=Solution()
A.isPalindrome("	")
A.isPalindrome("A man, a plan, a canal: Panama")
A.isPalindrome("ABCBA")
A.isPalindrome("abccba")