class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        """
        #Not Completed Solution
        def get_final( Tstr ):
            ansl=[]
            for x in Tstr:
                print('x:' , x)
                if x == '#':
                    print('he1')
                    try:
                        ansl.pop()
                    except:
                        pass
                else:
                    print('he2')
                    ansl.append(x)
                return ansl
        print('1: ', get_final(S), '2: ', get_final(T))
        return get_final(S) == get_final(T)
        """

        #OK solution
        sa, ta= [], []
        for x in S:
            if x == '#':
                try:
                    sa.pop()
                except:
                    pass
            else:
                sa.append(x)
        
        for y in T:
            if y == '#':
                try:
                    ta.pop()
                except:
                    pass
            else:
                ta.append(y)
                
        if sa == ta:
            print('T')
            return True
        return False
        
        """
        #Not Completed Solution
        sc=S.count('#')
        tc=T.count('#')
        sa=S
        ta=T
        for x in range(sc):
            print('1:', sa[0:sa.find('#')-1:])
            print('2:', sa[sa.find('#')+1::])
            sa=sa[0:sa.find('#')-1:]+sa[sa.find('#')+1::]
            print(sa)
        for y in range(tc):
            ta=ta[0:ta.find('#')-1:]+ta[T.find('#')+1::]
            print('3:',ta[0:ta.find('#')-1:])
            print('4', ta[T.find('#')+1::])
            print('ta:', ta)
        if sa == ta:
            print(True)
            return True
        return False
        """   


        """
        #Not Completed Solution
        sl=S.split('#')
        tl=T.split('#')
        print(sl, ' compare  ', tl)
        sa=""
        ta=""
        if sl[-1] == "":
            for x in range(len(sl)):
                sa=sa+sa[x][:-1]
        else:
            for x in range(len(sl)-1):
                sa=sa+sa[x][:-1]

        if tl[-1] == "":
            for x in range(len(tl)):
                ta=ta+ta[x][:-1]
        else:
            for x in range(len(tl)-1):
                ta=ta+ta[x][:-1]
        print("F:", sa, "  ", ta)
        """
		
A=Solution()
A.backspaceCompare("ab##", "c#d#")