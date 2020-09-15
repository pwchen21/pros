class Solution:  
    def islandPerimeter(self, grid):
        #print('grid', len(grid))
        ans = 0
        for x in range(len(grid)):
            #print('x:', x)
            for y in range(len(grid[0])):
                #print('  y:',y)
                
                if grid[x][y] == 1:
                    ans +=4
                    #print('        ans-is1:', ans)
                    if y!=len(grid[0])-1 and grid[x][y+1]==1:
                        #print('     right')
                        ans-=1
                        #print('         ans-r:', ans)

                    if y!=0 and grid[x][y-1]==1:
                        #print('     left')
                        ans-=1
                        #print('         ans-l:', ans)

                    if x!= len(grid)-1 and grid[x+1][y]==1:
                        #print('     down')
                        ans-=1
                        #print('         ans-d:', ans)

                    if x!=0 and grid[x-1][y]==1:
                        #print('     up')                            
                        ans-=1
                        #print('         ans-l:', ans)

                        
        print(ans)
         
        
A=Solution()
A.islandPerimeter([[0,1,0,0], [1,1,1,0], [0,1,0,0],[1,1,0,0]])