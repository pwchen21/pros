class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        res = sorted([int(x) for x in str(N)])
        print(1, res)
        for i in range(30):
            print(2, i, str(1<<i))
            print(2, sorted([int(x) for x in str(1 << i)]))
            if sorted([int(x) for x in str(1 << i)]) == res:
                return True
        return False


A=Solution()
A.reorderedPowerOf2(3412)