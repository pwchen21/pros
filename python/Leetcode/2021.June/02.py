class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str):
        s1_l, s2_l, s3_l = len(s1), len(s2), len(s3)
        print(s1_l, s2_l, s3_l)
        if s3_l != s1_l + s2_l: return False
        

        def rec(x, y, z):
            print(x, y , z)
            if x == s1_l and y == s2_l and z == s3_l:
                print('OK')
                return True
            
            s1_b, s2_b=False, False
            if x < s1_l and s1[x] == s3[z]:
                print('1-----')
                s1_b=rec(x+1, y, z+1)
            if y < s2_l and s2[y] == s3[z]:
                print('2------')
                s2_b=rec(x, y+1, z+1)

            return s1_b or s2_b

        #print(rec(0, 0, 0))
        return(rec(0, 0, 0))


A=Solution()
A.isInterleave("aabcc", "dbbca", "aadbbcbcac")
print('===')
A.isInterleave("aabcc", "dbbca", "aadbbbaccc")