class Solution(object):
    def isToeplitzMatrix(self, matrix):
		for x in range(len(matrix)-1):
			for y in range(len(matrix[0])-1):
				print 'x, y, v:' , x , y , matrix[x][y]
				print 'v+1:',  matrix[x+1][y+1]
				if matrix[x][y] != matrix[x+1][y+1]:
					print False
		print True
	

A=Solution()
A.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])