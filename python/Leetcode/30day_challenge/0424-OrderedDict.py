from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.c=capacity
        self.dic=OrderedDict()

    def get(self, key: int) -> int:        
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key]=value
            self.dic.move_to_end(key)
        else:
            if len(self.dic) == self.c:
                self.dic.popitem(last=False)
                self.dic[key]=value
            else:
                self.dic[key]=value