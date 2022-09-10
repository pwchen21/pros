# copy from python app
class Solution:
    def minDominoRotations(self, tops, bottoms):
        n = len(tops)
        for num in range(1,7):
            if all (a == num or b == num for a, b in zip(tops, bottoms)):
                print(min(n-tops.count(num), n-bottoms.count(num)))
            
        return -1

A=Solution()
A.minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2] )