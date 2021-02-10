class Solution:
    def rotate(self, matrix):
    	# * unzipped , -1 rotate
        matrix[:] = zip(*matrix[::-1])
        print(matrix)

A=Solution()
A.rotate([[1,2,3],[4,5,6],[7,8,9]])