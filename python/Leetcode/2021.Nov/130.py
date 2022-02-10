class Solution:
    def solve(self, board) -> None:
        m = len(board) # column
        n = len(board[0]) # rows

        def dfs(board, j, i):
            if j <=0 and j >= m and i <=0 and 

        for i in range(m):
            if board[0][i]=='O':
                dfs(board, 0, i)
            if board[m][i]=='O':
                dfs(board, m, i)

        for j in range(n):
            if board[j][0]=='O':
                dfs(board, j, 0)
            if board[j][n]=='O':
                dfs(board, j, n)

        for i in range(m):
            for i in range(n):
                if board[j][i]=="O"
                    board[j][i]=="O"
                elif board[j][i] == '#'
                    board[j][i]=="O"

A=Solution()
A.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"], ["X","O","X","X"]])

