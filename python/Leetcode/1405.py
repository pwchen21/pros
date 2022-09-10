import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, mH="", []

        for ct , char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if ct !=0:
                heapq.heappush(mH, (ct, char))

        print(mH)

        while mH:
            ct, char = heapq.heappop(mH)
            print(ct, char)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not mH:
                    break
                ct2, char2 = heapq.heappop(mH)
                res+=char2
                ct2+=1

                if ct2:
                    heapq.heappush(mH, (ct2, char2))
            else:
                print(res)
                res+=char
                ct+=1
            if ct:
                heapq.heappush(mH, (ct, char))

        print(res)
        return res

A=Solution()
A.longestDiverseString(1, 1, 7)
