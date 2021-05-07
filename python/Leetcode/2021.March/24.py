#Accpted Answer , but time is not good enough
class Solution:
    def advantageCount(self, A, B):
        sa=sorted(A)
        res=[]
        for x in B:
            t=0
            for y in sa:
                if y > x:
                    res.append(y)
                    sa.remove(y)
                    t=1
                    break
            if t==0:
                res.append(sa[0])
                sa.remove(sa[0])

        print(res)



A=Solution()
A.advantageCount([12,24,8,32],[13,25,32,11])