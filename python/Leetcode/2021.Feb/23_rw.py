class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix) and len(matrix[0])
        print('1:', m,'/', n)
        r, c = 0, n-1
        print('2:', r,'/', c)
        while r < m and c >= 0:
            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else: return True
        return False


A=Solution()
A.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 14)