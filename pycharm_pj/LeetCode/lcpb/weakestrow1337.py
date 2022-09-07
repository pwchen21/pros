class Solutions():
    def kWeakestRows(self, mat, k):
        sum_n=[[i, sum(g)] for i, g in enumerate(mat)]
        sum_n.sort(key=lambda s : s[1])
        #print([sum_n[x][0] for x in range(k)])
        return [sum_n[x][0] for x in range(k)]



#A=Solutions()
#A.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3)
