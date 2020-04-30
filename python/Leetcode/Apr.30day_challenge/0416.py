class Solution:
    def numIslands(self, grid):
        self.eg=grid
        self.isc=0   #Island conut
        self.irag=[] #Island range
        self.lo=len(self.eg)
        self.it=len(self.eg[0])
        self.chkstp(self.eg)
        
    def chkstp(self, grid):
        print('=Check start point=')
        for lows in range(self.it):
            for items in range(self.lo):
                print('1.Find island start:', items,lows, '\n')
                self.iragc(items, lows)
                break
            break
                
    def iragc(self, stpl, stpr):
        print('=iragc check=')
        self.rtl, self.utd, self.rutld = 0, 0, 0
        
        for x in range(self.it):
            if self.eg[stpl][x] == 1:
               print('RTL:', stpl, x)
               self.eg[stpl][x] = 0
               rtl +=1
        
        for y in range(self.lo):
            if self.eg[y][stpr] == 1:
               print('UTD:', y, stpr)
               self.eg[y][stpr] = 0
               self.utd +=1               
        
        for z in range(stpl):
            for w in range(stpr):
                print("rutld:", z , w)
                if self.eg[z][w] == 1:
                   self.eg[z][w] = 0
                   selt.rutld+=1
        
        print('rtl, utd, rutld:', self.rtl, self.utd, self.rutld)
        print("2.eg(grid) now:", self.eg ,'\n')    
        print("3. count", self.isc, '\n')
A=Solution()
A.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])