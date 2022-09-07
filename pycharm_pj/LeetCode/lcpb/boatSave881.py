class Solution:
    def numRescueBoats(self, people, limit):
        boats=0
        people.sort()
        light, heavy = 0, len(people) -1
        while light <= heavy:
            boats+=1
            if people[light]+people[heavy] <= limit:
                light+=1
            heavy -=1

        return boats


        """
        # Should be correct answer but time exceed.
        people=sorted(people, reverse=True)
        #svp=[]
        ans=0
        #while len(svp) != people and people:
        while people:
            ans+=1
            temp=people[0]
            #svp.append(temp)
            people.remove(temp)
            if temp < limit:
                for x in people:
                    if x + temp <= limit:
                        #svp.append(x)
                        people.remove(x)
                        break

        """

        return ans