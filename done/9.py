class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        lx=list(str(x))
        
        if x < 0:
            return False
        
        if len(lx) % 2 == 0:
			#print '11', lx[0:len(lx)/2]
			A=lx[len(lx)/2:]
			A.reverse()
			#print '12', A
			return lx[0:len(lx)/2] == A
			
        else:
			#print '21', lx[0:len(lx)/2]
			#print '22', lx[len(lx)/2+1:]
			B=lx[len(lx)/2+1:]
			B.reverse()
			return lx[0:len(lx)/2] == B
			
A=Solution()
print ("====1====")
A.isPalindrome(13423431)
print ("====2====")
A.isPalindrome(1347431)