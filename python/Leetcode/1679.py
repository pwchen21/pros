from collections import Counter

class Solution:
    def maxOperations(self, nums, k):
        cnt, ans = Counter(nums), 0
        print('cnt:', cnt)
        for val in cnt:
            print('v:', val)
            ans += min(cnt[val], cnt[k - val])
            print('ans:', ans)
        return ans//2

A=Solution()
A.maxOperations([1,2,3,4,5,6,7], 6)