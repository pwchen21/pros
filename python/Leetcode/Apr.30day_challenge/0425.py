class Solution(object):
    def canJump(self, nums):
        print(nums)
        reach = 0
        for i, num in enumerate(nums):
            #print('i, num:', i , "," , num)
            if i > reach:
                return False
            reach = max(reach, i + num)
            #print('RN:', reach)
        return True

        
A=Solution()
A.canJump([3,2,1,0,4])