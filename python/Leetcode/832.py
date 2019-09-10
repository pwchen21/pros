class Solution(object):
    def flipAndInvertImage(self, A):
        
        for x in A:
            x.reverse()
            #print('A1:', A)
            #print('x:', x)
            for i in range(len(x)):
                if x[i] == 0:
                    x[i]=1
                else:
                    x[i]=0
        print(A)

Ans=Solution()
Ans.flipAndInvertImage([[1,1,0], [1,0,1], [0,0,0]])