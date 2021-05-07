class Solution:
    def validateStackSequences(self, pushed, popped):
        pi=0
        po=0
        temp=[]
        for x in popped[:]:
            print('pop, x:', x)
            if (len(temp)>=1) and (x == temp[-1]):
                    print('   1: temp', temp)
                    temp.pop()
            else:
                for y in pushed[pi:]:
                    print(' pi', pi, 'push', y)
                    if x == y:
                        print('  0:    x', x)
                        pi+=1
                        break
                    else:
                        pi+=1
                        temp.append(y)
                        print('2.', temp)
            po=0
        print(temp)


A=Solution()
A.validateStackSequences([1,2,3,4,5], [5,4,3,2,1])
print('=============')
A.validateStackSequences([1,2,3,4,5], [5,4,3,1,2])
print('=============')
A.validateStackSequences([1,2], [2])
print('=============')
A.validateStackSequences([2,3,0,1], [0,3,2,1])


