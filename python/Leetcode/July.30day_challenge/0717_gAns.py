import collections
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums        
        counter = collections.Counter(nums)

        """ Add by me
        print('0', counter)
        print('1-1', counter.keys())      
        print('1-2', counter.values())      
        print('2', counter.get)      
        """
        
        # Need to be reviewed
        return heapq.nlargest(k, counter.keys(), key = counter.get)
        
A=Solution()
A.topKFrequent([9,9,7,8,7,7,7], 2)