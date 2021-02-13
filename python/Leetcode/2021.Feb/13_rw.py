class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] or grid[-1][-1]:
            return -1
        m,n = len(grid),len(grid[0])
        queue = collections.deque([(0,0,1)])
        directions = [(0,1),(1,0),(0,-1),(0,1),(1,1),(-1,-1),(1,-1),(-1,1)]
        seen = set()
        while queue:
            i,j,steps = queue.popleft()
            if i == m - 1 and j == n - 1:
                return steps
            for dx,dy in directions:
                x,y = i+dx,j+dy
                if 0<=x<m and 0<=y<n and not grid[x][y]and (x,y) not in seen:
                    seen.add((x,y))
                    queue.append((x,y,steps+1))
        return -1
        #RW_needed