class Solution:
    def isSumEqual(self, fsw: str, scw: str, tw: str) -> bool:
        dic={'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'}
        comp1=0
        tmp=''
        for x in fsw:
            tmp+=dic[x]
            #print('1:', tmp)

        comp1+=int(tmp)
        
        tmp=''
        for y in scw:
            tmp+=dic[y]
            #print('2:', tmp)

        comp1+=int(tmp)

        #print(comp1)
        tmp=''
        for z in tw:
            tmp+=dic[z]

        comp2=int(tmp)

        #print(comp2)
        print(comp1==comp2)

A=Solution()
A.isSumEqual("acb", "cba", "cdb")