class Solution:
    def minRemoveToMakeValid(self, s):
        s=list(s)
        temp=[]
        for x in range(len(s)):
            if s[x] == '(':
                temp.append(x)
            elif s[x] == ')':
                if temp:
                    temp.pop()
                else:
                    s[x] = ''
        while temp:
            s[temp.pop()]=''

        print(''.join(s))
        return ''.join(s)

A=Solution()
#A.minRemoveToMakeValid('lee(t(c)o)de)')
# print('=======')
A.minRemoveToMakeValid('((a)(b))')
# print('=======')
#A.minRemoveToMakeValid('))((')
        