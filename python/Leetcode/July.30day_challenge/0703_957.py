class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        print("==T0==", 'days', cells, "=====")        
        tmp = cells.copy()
        loop = N % 14
        #print(loop)
        for y in range(1, loop+15):
        #for y in range(1, N+1):
            #print('cell:', cells)
            
            tmp[0] = 0
            tmp[7] = 0
            for x in range(1, 7, 1):
                #print('x:', x, 'front', cells[x-1], 'after', cells[x+1])
                if cells[x-1] == cells[x+1]:
                    tmp[x] = 1
                    #print('cells now:', cells)
                    #print('SET tmp[', x, '] to', 1, ":" , tmp)
                else:
                    tmp[x] = 0
                    #print('cells now:', cells)
                    #print('SET tmp[', x, '] to', 0, ":" , tmp)

            cells=tmp.copy()
            print("===", y, 'days', cells, "=====")
            
                
                    
        
T=Solution()
T.prisonAfterNDays([1,0,0,1,0,0,1,0], 826)