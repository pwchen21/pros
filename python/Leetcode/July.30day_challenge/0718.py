class Solution:
    def findOrder(self, numCourses, pre):
        if not pre:
            return [x for x in range(numCourses)]

            
        ans = []               
        for x in range(len(pre)):
            print('==For Rnd==', 'x=', x , 'item', pre[x])
            if pre[x][0] in ans:
                if pre[x][1] not in ans:
                    print('1', ans)
                    ans.insert(ans.index(pre[x][0]), pre[x][1])
                else:
                    if ans.index(pre[x][1]) > ans.index(pre[x][0]):
                        return []
            else:
                if (pre[x][1]) in ans:
                    print('t', ans.index(pre[x][1])+1)
                    ans.insert(ans.index(pre[x][1])+1, pre[x][0])
                    print('2, ' , ans )
                else:
                    ans.append(pre[x][1])
                    ans.append(pre[x][0])
                    print('3, ' , ans)
        
        if len(ans) < numCourses:
            for y in range(len(ans), numCourses):
                ans.append(y)
        
        print(ans)
                
A=Solution()
A.findOrder(3, [[0,1],[0,2],[1,2]])