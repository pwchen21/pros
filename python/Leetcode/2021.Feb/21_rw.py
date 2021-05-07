class Solution:
    def brokenCalc(self, X, Y):
        if X > Y: return X - Y
        if X == Y: return 0
        if Y % 2 == 0:
            print('1y', Y)
            print('x, y//2+1: ', X, Y//2 + 1)
            return self.brokenCalc(X, Y//2) + 1
        else:
            print('2y', Y)
            print('X, Y+1: ', X , Y//2+1)
            return self.brokenCalc(X, Y + 1) + 1



A=Solution()
A.brokenCalc(3, 10)