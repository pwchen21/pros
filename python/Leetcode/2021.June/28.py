class Solution:
    def removeDuplicates(self, s: str) -> str:
        sl=S.lower()
        ans=[]
        for x in sl:
            if ans and ans[-1]==x:
                ans.pop()
            else:
                ans.append(x)
        return ''.join(ans)

A=Solution()
A.removeDuplicates('azxxzy')