class Solution:
    def largeGroupPositions(self, s):
        rs=[]
        start=0
        for i, c in enumerate(s):
            print(i, c)
            if i == len(s) -1 or c!= s[i+1]:
                if i - start >=2:
                    rs.append([start, i])
                start = i+1

        print(rs)


A=Solution()
A.largeGroupPositions("abbxxxxzzy")