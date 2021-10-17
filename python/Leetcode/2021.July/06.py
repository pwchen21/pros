class Solution:
    def kthSmallest(self, matrix, k):
        E=[]
        for x in matrix:
            for i in x:
                E.append(i)
        
        print(sorted(E)[k-1])
        return(sorted(E)[k-1])

A=Solution()
A.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)