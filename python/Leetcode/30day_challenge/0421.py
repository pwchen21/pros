class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n,m = binaryMatrix.dimensions();i = n-1;j= m-1
        while (i>=0 and j>=0):
            if binaryMatrix.get(i,j)==0 :i-=1
            else:j-=1
            
        return -1 if j == m-1  else j+1