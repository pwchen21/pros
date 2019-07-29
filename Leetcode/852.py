class Solution(object):
    def peakIndexInMountainArray(self, A):
        tp=0
        id=0
        print(A)
        for x in A:
            if x >= tp:
                tp=x
                id=id+1
                print('tp:', tp)
            else:
                print('A:',id-1)
                return(id-1)
        print(len(A)-1)
        return(len(A)-1)
A=Solution()
A.peakIndexInMountainArray([0,1,2])