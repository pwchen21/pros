# Check Magin 
# if Magin is 'O' check all direction is 'O'


class Solution:
    def solve(self, board) -> None:
        m = len(board)
        n = len(board[0])
        if m <= 2 or n <= 2:
            return;
    
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'B'
                print('ck:', 1, i+1, j)
                dfs(i + 1, j)

                print('ck:', 2, i-1, j)
                dfs(i - 1, j)

                print('ck:', 3, i, j+1)
                dfs(i, j + 1)

                print('ck:', 4, i, j-1)
                dfs(i, j - 1)

        for i in range(m):
            print('====R====')
            print(i)
            dfs(i, 0)
            dfs(i, n - 1)
            #print(board)

        for j in range(n):
            print('====C====')
            print(j)
            print('*', 0, j)
            dfs(0, j)
            print('#', m-1, j)
            dfs(m - 1, j)
            #print(board)

        for i in range(m):
            for j in range(n):
                c = board[i][j]
                #if c != 'X':
                #    if c=='B':
                #        board[i][j]='O'
                #    else:
                #        board[i][j]='X'
                if c != 'X':
                    board[i][j] = 'X' if c == 'O' else 'O'

        print('=Final Answer=')
        print(board)

A=Solution()
A.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"], ["X","O","X","X"]])

