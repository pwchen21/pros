class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        T=sorted(list(set(nums)))
        print(T)
        if len(T) >= 3:
            return T[-3]
        else:
            return T[-1]