class Solution:
    def lastStoneWeight(self, stones):
        stones.sort(reverse=True)
        while len(stones) > 1:
            a=stones[0]
            b=stones[1]
            if a == b:
                stones.remove(a)
                stones.remove(b)
            else:
                stones.remove(a)
                stones.remove(b)
                stones.append(abs(a-b))
                stones.sort(reverse=True)
        if stones:
            print(stones[0])        
            return(stones[0])        
        else:
            print(0)
            return 0


A=Solution()
A.lastStoneWeight([2,2])