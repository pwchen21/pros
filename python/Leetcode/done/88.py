class Solution(object):
    def merge(self, nums1, m, nums2, n):
		temp=nums1[0:m]+nums2[0:n]
		temp.sort()
		y=0
		for x in temp:
			#print 'x',x
			nums1[y]=x
			#print nums1
			y=y+1
		print nums1
		'''
		y=0
		for x in range(m, m+n):
			nums1[x]=nums2[y]
			y+=1
		print nums1
		'''
		
A=Solution()
A.merge([1,3,5,7,9,11], 3 , [10, 20, 30, 40, 50], 2)
#A.merge([2,0], 1 , [1], 1)