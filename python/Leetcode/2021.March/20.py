class UndergroundSystem:

    def __init__(self):
        self.ci={} #check-in time
        self.tt={} #total time

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ci[id]=[stationName, t] # record check-in information
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stc=self.ci[id][0]+'-'+stationName #start-end name
        if self.ci[id][0]+'-'+stationName not in self.tt:
            self.tt[stc]=[t-self.ci[id][1], 1] #add new start-end record to tt if not exists
        else:
            #if start-end exists
            self.tt[stc][0]+=t-self.ci[id][1] #update total time
            self.tt[stc][1]+=1 #update travel times with the same start-end
        del self.ci[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        sted=startStation+'-'+endStation #find start-end in tt
        if sted in self.tt:
            return  (self.tt[sted][0])/(self.tt[sted][1]) # start-end tatal time / travel times

#beats 95.68/99.59