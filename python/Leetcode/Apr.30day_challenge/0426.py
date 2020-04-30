class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ln=max(len(text1), len(text2))
        
        st=[x for x in (text1, text2) if ln==len(x)]
        stl=len(st[0])
        ss=list(st[0])
        print(st, '  ', stl, '  ', ss)
        
        lt=[x for x in (text1, text2) if st[0]==text1 else text1]
        ltl=len(lt[0])
        ls=list(lt[0])
        print(lt, '  ', ltl, '  ', ls)
        
        '''
        
        id=0        
        for x in ls:
            if x in ss:
                if x == ss[id]:
                    id+=1
                    if id == stl:
                        return stl
                else:
                    return 0
            return 0
         '''
         
A=Solution()
A.longestCommonSubsequence("abcde", "ace")