class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def test(s1, k1):
            print('==start==')
            ss=set(s1)
            print(ss)
            k=0
            for x in ss:
                print('1:', x, s1, x*k1)
                print('2:', s1.find(x*k1))
                if s1.find(x*k1) != -1:
                    print('find:', x*k1)
                    key=s1.find(x*k1)
                    print('key', key)
                    s1=s1[:key]+s1[key+k1:]
                    print('s1 removed:', s1)
                    k=1
            if k==0:
                print('no more')
                return s1

            return test(s1, k1)

        print('ans is:', test(s, k))

A=Solution()
A.removeDuplicates("deeedbbcccbdaa", 3)