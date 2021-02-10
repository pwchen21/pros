class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res=haystack.find(needle)
        if res == -1:
        	return 0
        else:
        	return res

A=Solution()
A.strStr("hello", "bb")