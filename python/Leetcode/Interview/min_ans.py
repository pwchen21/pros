class Solution:
    def minOperations(self, nums,x):
        arr_sum = sum(nums)
        print('1. arr_sum', arr_sum)
        if arr_sum < x:
            return -1
        if arr_sum == x:
            return len(nums)
        
        required_subarray_sum = arr_sum - x
        print('2. required_subarray_sum:', required_subarray_sum)
        left = curr_sum = max_subarray_size = 0
        for right, num in enumerate(nums):
            print('3. right, num: ', right, ' ', num)
            curr_sum += num
            print('4. curr_sum:', curr_sum)
            while curr_sum > required_subarray_sum:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == required_subarray_sum:
                max_subarray_size = max(max_subarray_size, right - left + 1)
                
        return len(nums) - max_subarray_size if max_subarray_size > 0 else -1

A=Solution()
A.minOperations([3,2,20,1,1,3], 10)