board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

col=len(board[0])
row=len(board)
print('col:', col)
print('row', row)
cc=[]

for r in range(row):
    for c in range(col):
        ct=0
        print('local:(', r, c , ') value:', board[r][c])
        for (x, y) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]:
            #if r+x < 0 or c+y < 0 or r+x > row or c+y > col:
            #print('r', r, 'x', x, 'c', c, 'y', y)
            if r+x >= row or c+y >= col or r+x <0 or c+y<0:
                print('A', r+x, c+y, 0)
            else:
                if board[r+x][c+y] == 1:
                    ct +=1
                print('B', r+x, c+y, board[r+x][c+y])

        print('ct:', ct)

        #Rule1:
        if ct < 2 and board[r][c] == 1 :
            cc.append([r,c])
            print('rule1:', r, c)
            #board[r][c] = 0
        #Rule2:
        #elif 2<= ct < 3 and board[r][c] !=1:
        #    cc.append([r, c])
        #    print('rule2:', r, c)

        #Rule3:
        if ct > 3 and board[r][c] == 1:
            cc.append([r, c])
            print('rule3:', r, c)

        #Rule4:
        if ct ==3 and board[r][c] == 0:
            cc.append([r, c])
            print('rule4:', r, c)


for ch in cc:
    print('ch', ch)
    print(ch[0], ch[1])
    if board[ch[0]][ch[1]] == 0:
        #print('change')
        board[ch[0]][ch[1]]=1
        #print('board[', ch[0], '][', ch[1], ']')
    else:
        board[ch[0]][ch[1]]=0

print(board)