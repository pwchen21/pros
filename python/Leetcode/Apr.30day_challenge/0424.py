class LRUCache:

    def __init__(self, capacity: int):
        self.c=capacity
        self.dic={}
        self.lst=[]

    def get(self, key: int) -> int:
        if key in self.dic:
            if key not in self.lst:
                self.lst.append(key)
            else:
                self.lst.remove(key)
                self.lst.append(key)

            if len(self.lst) > self.c:
                self.lst.remove(self.lst[0])

            #print("--1--")
            #print(self.dic)
            #print(self.lst)
            return self.dic[key]
        else:
            return -1
        

        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key]=value
            if key in self.lst:
                self.lst.remove(key)
                self.lst.append(key)
            else:
                self.lst.remove(lst[0])
                self.lst.append(key)
        else:
            if len(self.dic) >= self.c:
                self.dic.__delitem__(self.lst[0])
                self.lst.remove(self.lst[0])
                self.dic[key]=value
                self.lst.append(key)
            else:
                self.dic[key]=value
                self.lst.append(key)

        #print("--2--")
        #print(self.dic)
        #print(self.lst)
                    