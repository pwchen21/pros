class Solution:
    def isBipartite(self, graph):
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
                        break
                    elif j in v:
                        tg='u'
                        u.append(temp)
                        break
                    else:
                        u.append(temp)
            temp+=1
            
            print('tg:', tg)
            print('u:' , u, '   v: ', v)

            for y in x:
                if tg == 'u':
                    if y in u:
                        print(False)
                        #return False
                    if y not in v:
                        v.append(y)

                else:
                    if y in v:
                        print(False)
                        #return False
                    if y not in u:
                        u.append(y)

                print('u:' , u, '   v: ', v)
        print(True)    
        #return True
                    
A=Solution()
A.isBipartite([[1,3],[0,2],[1,3],[0,2]])
print('========')
A.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
print('========')
A.isBipartite([[1],[0,3],[3],[1,2]])
                