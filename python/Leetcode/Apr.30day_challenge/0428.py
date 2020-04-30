class FirstUnique:

    def __init__(self, nums: List[int]):
        #print('First:', nums)
        self.fst=nums
        self.tmp = []
        for x in nums:
            if self.fst.count(x) == 1:
                self.tmp.append(x)      
        #print('keys', self.tmp)
        
    def showFirstUnique(self) -> int:
        temp=-1
        #print(self.fst)
        #print('=', list(set(self.fst)))        
        for x in self.tmp[:]:
            if self.fst.count(x) == 1:
                if temp == -1:
                    temp = x
                else:
                    #print('1', temp)
                    return temp
            else:
                self.tmp.remove(x)
        #print('2', temp)
        return temp


    def add(self, value: int) -> None:
        self.fst.append(value)
        if value not in self.tmp:
            self.tmp.append(value)
        #print('3',self.fst)
