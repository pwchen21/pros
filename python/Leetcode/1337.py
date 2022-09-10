class Solutions():
    def kWeakestRows(self, mat, k):
        sum_n=[[i, sum(g)] for i, g in enumerate(mat)]
        print(sum_n, k)


A=Solutions()
A.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 1)
