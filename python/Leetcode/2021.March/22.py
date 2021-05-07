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
                

            print(ans)


A=Solution()
A.spellchecker(["v","t","k","g","n","k","u","h","m","p"], ["n","g","k","q","m","h","x","t","p","p"])
A.spellchecker(["KiTe","kite","hare","Hare"],["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])