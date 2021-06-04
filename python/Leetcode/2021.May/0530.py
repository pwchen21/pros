class Solution:
    def maximumGap(self, nums):
        s=sorted(nums)
        print('sorted:', s)
        last=s[0]
        mx=0
        if len(nums) <=1:
            return 0
        for x in s:
            print('mx now', mx)
            print('last', last)
            print('x', x)
            if x - last >= mx:
                mx = x - last
                print('mx', mx)
        
            last = x
        print(mx)
        return mx
        

A=Solution()
A.maximumGap([3,1,6,9])