class Solution:
    def twoCitySchedCost(self, costs):
        ans=0
        l=len(costs)//2
        costs.sort(key=lambda s : s[0] - s[1])
        for x in costs[:l]:
            #print(x, x[0])
            ans+=x[0]

        for y in costs[l:]:
            #print(y, y[1])
            ans+=y[1]

        return(ans)


#A=Solution()
#A.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
