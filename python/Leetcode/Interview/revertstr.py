class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        t=0
        print(len(s))
        for x in range(len(s)):
            x=s.pop()
            print(x)
            s.insert(t,x)
            t+=1
            print(s)

A=Solution()
A.reverseString(["H","a","n","n","a","h"])