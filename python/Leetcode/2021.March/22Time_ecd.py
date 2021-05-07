# Time exceed

class Solution:
    def spellchecker(self, wordlist, queries):
        ans=[]
        for que in queries:
            print(0, que)
            ans.append("")
            for wl in wordlist:
                print("  " , 1, wl)
                if que == wl:
                    ans[-1]=wl
                    print("     2", ans)
                    break
                elif que.upper() == wl.upper() and ans[-1]=="":
                    ans[-1]=wl
                    print('         3', ans)
            
            if ans[-1] == "":
                print('here1')
                for wl in wordlist:
                    print('     4', wl)
                    t, y = 0, 0
                    while y == 0:
                        print('         4',que[t], wl[t])
                        if que[t].lower() in ['a','e','i','o','u']:
                            if wl[t].lower() not in ['a','e','i','o','u']:
                                y=1
                                print('        4-1:')
                        else: 
                            if que[t].lower() != wl[t].lower():
                                y=1
                                print('        4-2:')
                        
                        if t==len(wl)-1 and y == 0:
                            ans[-1]=wl
                            print('             4-3', ans)
                            y=1
                        t+=1
                    if ans[-1] != "":
                        break

            print(ans)


A=Solution()
A.spellchecker(["v","t","k","g","n","k","u","h","m","p"], ["n","g","k","q","m","h","x","t","p","p"])
A.spellchecker(["KiTe","kite","hare","Hare"],["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])