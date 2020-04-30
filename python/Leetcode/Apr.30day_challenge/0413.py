class Solution:
    def findMaxLength(self, nums):
        ts = 0
        im = dict({0:-1})
        ans = 0  
        for i, num in enumerate(nums):
            if num == 0:
                ts -= 1
            else:
                ts += 1
            if ts in im:
                ans = max(ans, i - im[ts])
            else:
                im[ts] = i
        return ans
        """
        tmp_len=0
        ans=0
        ct0=0
        ct1=0
               
        for x in nums:
            print('===x:', x)
            if x == 0:
                ct0 += 1  
                print('ct0:', ct0)

            if x == 1:
                ct1 += 1
                print('ct1:', ct0)
        
            if ct0 == ct1:
                tmp_len = ct0 + ct1
                print('tmp_len', tmp_len)
            
            if ans < tmp_len:
                    ans = tmp_len                            
            else:
                tmp_len == 0
        print('ans:', ans)
        return(ans)
        """
A=Solution()
A.findMaxLength([0,0,1,0,0,0,1,1])