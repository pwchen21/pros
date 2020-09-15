class Solution:
    def exist(self, b, w):
        if not b or not b[0]: return False
        bc = Counter(chain(*b))
        wc = Counter(w)
        if any(c > bc[s] for s, c in wc.items()): return False
        m, n, wl = len(b), len(b[0]), len(w) - 1
        def dfs(d: int, x: int, y: int) -> bool:
            if w[d] != b[y][x]: return False
            if d == wl: return True
            c, b[y][x] = b[y][x], ''
            if x > 0 and dfs(d + 1, x - 1, y): return True
            if x < n-1 and dfs(d + 1, x + 1, y): return True
            if y > 0 and dfs(d + 1, x, y - 1): return True
            if y < m-1 and dfs(d + 1, x, y + 1): return True
            b[y][x] = c
            return False
        return any(dfs(0, j, i) for i in range(m) for j in range(n) if w[0] == b[i][j])