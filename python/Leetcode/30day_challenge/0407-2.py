class Solution:
    def groupAnagrams(self, strs):
        dict={}
        for x in strs:
            t=tuple(sorted(x))
            if t not in dict.keys():
                dict[t]=[x]
            else:
                dict[t].append(x)
        print(dict.values())
                    
A=Solution()
A.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])