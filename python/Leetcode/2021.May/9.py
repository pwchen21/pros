class Solution:
    def superpalindromesInRange(self, left, right):
        ans = 0
        temp=[]
        for x in range(left, right+1):
            print('1', x)
            if (x ** 0.5) % 1 == 0:
                t=str(x)
                print(' 2', t, len(t)%2)
                if len(t) % 2 == 0:
                    print('   3', len(t)%2)
                    for y in range(int(len(t)/2)):
                        print('     4', y,":",t[y], '  ', -y-1, ':', t[-y-1])
                        if t[y] != t[-y-1]:
                            break
                        print('-------ans+1')
                        ans+=1
                else:
                    print('     5', int((len(t)-1)/2))
                    for y in range(int((len(t)-1)/2)):
                        print('     5', y,":",t[y], '  ', -y-1, ':', t[-y-1])
                        if t[y] != t[-y-1]:
                            print('56')
                            break
                        print('----------ans+1')
                        ans+=1

        print(ans)

A=Solution()
A.superpalindromesInRange(4, 1000)