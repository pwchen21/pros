from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for i in strs:
            ans[tuple(sorted(i))].append(i)
            print(ans)

                    
A=Solution()
A.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])