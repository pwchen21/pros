class Solution:
    def searchMatrix(self, matrix, target):
    	#row, col=len(matrix), len(matrix)
    	row, col=len(matrix)-1,len(matrix[0])-1
    	print('1:', row, col)
    	ans=False
    	mal=len(matrix)-1

    	if target > matrix[mal][mal]:
    		print('a')
    		return False

    	print('b', row, col)

    	while matrix[row][col] >= target:
    		print(' 2:', row, col)
    		if matrix[row][col]==target:
    			print(True)
    			return True
    		if row != 0 and col != 0:
    			row-=1
    			col-=1
    		elif row !=0 :
    			col-=1
    		else:
    			row-=1
    	print()
    	'''
    	for x in range(row, -1, -1):
    		for y in range(col, -1, -1):
    			print('[', x, y, ']|[', y, x, ']', matrix[x][y])
    			if matrix[x][y]==target or matrix[y][x]==target:
    				print(True)
    				return True
    		break

    	print(False)
    	return False  			
		'''

A=Solution()
A.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
# [1,4,7,11,15]
# [2,5,8,12,19]
# [3,6,9,16,22]
# [10,13,14,17,24]
# [18,21,23,26,30]
        