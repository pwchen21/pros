#Correct answer but time exceed
class Solution:
    def originalDigits(self, s: str) -> str:
        ans=''
        ls=list(s)
        t=0
        dic={'0':'zero', '1':'one', '2':'two',  '3':'three', '4':'four',
        '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
        dic2={'z':'0', 'w':'2', 'u':'4', 'x':'6', 'g':'8', 'r':'3', 'o':'1', 'f':'5', 'i':'9', 's':'7'}
        #duplicate: e, r, o, t, h, f, i, v, n
        # e: 1, 3, 5, 7 , 9 /0, 8
        # r: 3 / 0
        # o: 1/ 0,2,4
        # t: 3/ 2,8
        # h: 3/ 8
        # f: 5 / 4
        # i: 5,9 / 6
        # v: 5, 7
        # n: 1, 7, 9
        # s: 7 / 6
        #nonduplicate: z(0), w(2), u(4), x(6), g(8)
        for x in ['z', 'w', 'u', 'x', 'g', 'r', 'o', 'f', 'i', 's']:
            t=ls.count(x)
            for y in range(t):
                for z in dic[dic2[x]]:
                    ls.remove(z)
                ans+=str(dic2[x])
                t-=1
        print(ls)
        print(ans)


A=Solution()
A.originalDigits("owoztneoer")
#96

