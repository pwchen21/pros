from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        for i, n in enumerate(nums):
            nums[i]=str(n)
            
        print(nums)

        def compare(n1,n2):
            print(n1, n2)
            if n1+n2>n2+n1:
                print("  N", n1+n2)
                return  -1
            else:
                print("  swap:", n2+n1)
                return 1



        nums=sorted(nums, key=cmp_to_key(compare))
        print(nums)
        return str(int("".join(nums)))

A=Solution()
A.largestNumber([3,34,30,9,5])
print("---------")
A.largestNumber([3,30,34,5,9])
