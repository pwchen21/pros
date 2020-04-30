class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ss=sorted(stones)
        while len(ss) > 1:
            ss.append(abs(ss.pop() - ss.pop()))
            ss=sorted(ss)
        return ss[0]