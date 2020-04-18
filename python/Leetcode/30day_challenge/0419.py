class Solution:
    def minPathSum(self, grid):
        M, N = len(grid), len(grid[0])
        for i in range(M):
            if i > 0:
                grid[i][0] = grid[i][0] + grid[i-1][0]
            
            else:
                grid[i][0] = grid[i][0]

            print('==')
            print(grid[i][0])                
            
            for j in range(1,N):
                if i > 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                    print('==')
                    print(grid[i][j])
                else:
                    grid[i][j] = grid[i][j-1]+grid[i][j]
        
        return grid[-1][-1]

A=Solution()
A.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
