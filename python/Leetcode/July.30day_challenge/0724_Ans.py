class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = [[0]]
        res = []
        while len(q) > 0:
            current = q.pop(0)
            if current[-1] == len(graph) - 1:
                res.append(current)
                continue
            for neighbor in graph[current[-1]]:
                q.append(current + [neighbor])
        
        return res