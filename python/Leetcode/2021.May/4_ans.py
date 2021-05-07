
class Solution:
    def checkPossibility(self, N):
        # Copy Code from disscussion
        err = 0
        for i in range(1, len(N)):
            if N[i] < N[i-1]:
                if err or (i > 1 and i < len(N) - 1 and N[i-2] > N[i] and N[i+1] < N[i-1]):
                    return False
                err = 1
        return True

A=Solution()
# print('---Ans is:', A.checkPossibility([1]) == True)
# print('---Ans is:', A.checkPossibility([4,2,3]) == True)
# print('---Ans is:', A.checkPossibility([2,4,3]) == True)
# print('---Ans is:', A.checkPossibility([1,2,3,4]) == True)
# print('---Ans is:', A.checkPossibility([4,3,2,1]) == False)
# print('---Ans is:', A.checkPossibility([4,2,1]) == False)
# print('---Ans is:', A.checkPossibility([1,4,8,7,8]) == True)
# print('---Ans is:', A.checkPossibility([1,4,8,7,10]) == True)
# print('---Ans is:', A.checkPossibility([3,4,2,3]) == False)
print('---Ans is:', A.checkPossibility([-1,4,2,3]) == True)
# print('---Ans is:', A.checkPossibility([1,2,5,3,3]) == True)


