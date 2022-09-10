import re

class Solution:
    def isSubsequence(self, s, t):
        p, tp=-1, -1
        
        for x in s:
            #print(x)
            if x in t and t.rfind(x) > p:
                #print(1, p , tp)
                sta = re.finditer(x, t)
                for index in sta:
                    if index.start() > p:
                        #print(2)
                        p=index.start()
                        tp=p
                        break
            else:
                print('False')
                return False
        
        print('True')
        return True

#A=Solution()
#A.isSubsequence("ab", "baaaaab")
#A.isSubsequence("ab", "baaaa")
#A.isSubsequence("abc", "ahbgdc")
