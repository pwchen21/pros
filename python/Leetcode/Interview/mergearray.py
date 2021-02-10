class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        print('x:', nums1)
        for ct in range(n):
            print('a. nums2', nums2[ct])
            for y in nums1[:]:
                print('b', y)
                if nums2[ct] > nums1[-1]:
                    nums1.append(nums2[ct])
                elif nums2[ct] <= y:
                    print('c. nums2, y', nums2[ct], y)
                    nums1.insert(nums1.index(y), nums2[ct])
                    print('d.temp', nums1)
                    break
            if not nums1:
                nums1.append(nums2[ct])
                        
        del nums1[m+n:]
        print(nums1)
        return nums1
            
A=Solution()
#A.merge([1],1,[],0)
A.merge([0],0,[1],1)