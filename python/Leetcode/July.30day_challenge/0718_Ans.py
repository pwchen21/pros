class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        ourDegree = {i:0 for i in range(numCourses)}
        for i,j in prerequisites:
            graph[i].append(j)
            ourDegree[j] += 1
        
        queue = deque()
        for i in ourDegree:
            if ourDegree[i] == 0:
                queue.append(i)
                
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for i in graph[node]:
                ourDegree[i] -= 1
                if ourDegree[i] == 0:
                    queue.append(i)
        if len(result) != numCourses: return []
        return result[::-1]