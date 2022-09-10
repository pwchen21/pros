from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        print(anagrams)
        for s in strs:
            sorted_str = "".join(sorted(s))
            anagrams[sorted_str].append(s)
            print(anagrams)
        return list(anagrams.values())

        # gp={}
        # ans=[]
        # for x in strs:
        #     print("--")
        #     t=''.join(sorted(x))
        #     print(gp.values())
        #     print("t:",t)
        #     if t in gp:
        #         gp[t].append(x)
        #     else:
        #         gp[t] = [x]

        #     print(gp)
        
        # ans = gp.values()
        # print(list(ans))

A=Solution()
A.groupAnagrams(["eat","tea","tan","ate","nat","bat"])