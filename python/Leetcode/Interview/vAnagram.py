class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for x in set(s):
            if s.count(x) != t.count(x):
                print('F')
                return False
        print('T')
        return True


A=Solution()
A.isAnagram("cat", "car")