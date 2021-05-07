class FreqStack:

    def __init__(self):
        self.ans=[]
    
    def push(self, x: int) -> None:
        self.ans.append(x)
        #print('push:', self.ans)

    def pop(self) -> int:
        mx=0
        att=[]
        T=list(set(self.ans))
        #print("===", 'SET is ', T , '===')
        
        for x in T:
            #print(' check count in SET:', x)
            #print('==', self.ans.count(x))
            if self.ans.count(x) > mx:
                att=[]
                mx=self.ans.count(x)
                att.append(x)
                #print('   1. append:',att, ' mx:', mx)
            elif self.ans.count(x) == mx:
                att.append(x)
                #print('   2. Same count append:', att,' mx:', mx)
            else:
                #print('   3.skip',  att )
                continue
                
        for y in range(len(self.ans)-1, -1, -1):
            #print('    Check ans now:', self.ans[y])
            if self.ans[y] in att:
                anst=self.ans[y]
                del self.ans[y]
                #print('      4.', anst)
                return anst
            
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


