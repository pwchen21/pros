class Solution:
    def groupAnagrams(self, strs):
        gr={}
        ans=[]
        ct=0
        for x in strs:
            print('===strs:', x)
            tl=sorted(list(x))
            sortx="".join(tl)
            if sortx not in gr.keys():
                gr[sortx]=ct
                print('gr now:', gr)
                ans.append([x])
                ct+=1
            else:
                ans[gr[sortx]].append(x)
                print('not creae gr!')

            print(ans)


                    
A=Solution()
A.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])