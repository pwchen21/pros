class Solution:
    def maxProfit(self, prices):
        count=[]
        max=0
        st=0
        for i in range(len(prices)):
            print('i:', i)
            temp=[]
            for x in prices[i+1:]:
                Test=[]            
                #print('How many 0?', (i+1))
                Test.extend([0]*(i+1))
                #print(Test)
                if x > prices[i]:
                    temp.append(x-prices[i])
                else:
                    temp.append(0)
                
                Test=Test+temp
            print(Test)
            
            count.append(Test)
            #print(count)
            #temp=[prices[i]-prices[i] for x in prices[i+1:]]
            #print(temp)
            #AAA=[[0]*(i+1), temp]
            #print(AAA)
        print('==========')    
        for g in count:
            for h in count[g]:
                if h !=0:
                    st = h
        
Test=Solution()
Test.maxProfit([7,1,5,3,6,4])	