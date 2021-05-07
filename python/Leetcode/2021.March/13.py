class Solution:
    def numFactoredBinaryTrees(self, A):
        t = {}
        for a in sorted(A):
            print('1:', a)
            # for b in A:
            #     print('b', b)
            #     if b < a:
            #         n=sum(t[b]*t.get(a/b, 0))
            #         print(n)
            t[a] = 1 + sum(t[b] * t.get(a/b, 0) for b in A if b < a)
            print('2:   ', t[a])
        return sum(t.values()) % (10**9 + 7)


A=Solution()
A.numFactoredBinaryTrees([4,2,6,8,10])