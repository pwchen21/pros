class PeekingIterator:
    def __init__(self, iterator):
        self.iter=iterator
        if self.iter.hasNext():
            self.nt=self.iter.next()
        else:
            self.nt=None
    
    def peek(self):
        return self.nt
    
    def next(self):
        nnt=self.nt
        if self.iter.hasNext():
            self.nt=self.iter.next()
        else:
            self.nt=None
        return nnt
    
    def hasNext(self):
        return self.nt is not None