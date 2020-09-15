from collections import OrderedDict

class Solution:
    def topKFrequent(self, nums, k):
        s=set(nums)
        D=OrderedDict()
        ans=[]
        for x in s:
            D[x]=nums.count(x)
            
        nD=OrderedDict(sorted(D.items(), key=lambda x: x[1]))
        print(nD)
        
        for x in range(k):
            ans.append(nD.popitem()[0])
         
        print('ans', ans)
         
A=Solution()
A.topKFrequent([9,9,7,8,7,7,7], 2)