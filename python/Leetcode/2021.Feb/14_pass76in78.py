class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        u,v = [],[]
        temp = 0
        tg=''
        for x in graph:
            if temp in u:
                tg='u'
            elif temp in v:
                tg='v'
            else:
                for j in x:
                    if j in u:
                        tg='v'
                        v.append(temp)
                        
                    elif j in v:
                        tg='u'
                        u.append(temp)
                    else:
                        tg='u'
                        u.append(temp)
                    break
            temp+=1

            for y in x:
                if tg == 'u':
                    if y in u:
                        return False
                    if y not in v:
                        v.append(y)

                else:
                    if y in v:
                        return False
                    if y not in u:
                        u.append(y)

        return True