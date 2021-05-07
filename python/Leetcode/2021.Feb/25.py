class Solution:
	def findUnsortedSubarray(self, nums):
		a, b=0, 0
		temp=sorted(nums)
		for x in range(len(nums)):
			if nums[x] != temp[x]:
				a=x
				break
		for y in range(len(nums)-1,0,-1):
			if nums[y] != temp[y]:
				b=y
				break

		print(a,b)

		if a !=0 or b!=0:
			print(b-a+1)            
			return b-a+1
		else:
			print(0)
			return 0
		'''
		#OK
		tl=[]
		temp=sorted(nums)
		for x in range(len(nums)):
			if nums[x] != temp[x]:
				tl.append(x)

		if tl:
			print(tl[-1]-tl[0]+1)
		else:
			print(0)
			return 0
		'''
		'''
		temp=[]
		last=0
		for x in range(len(nums)):
			if nums[x] < last:
				temp.append(x-1)
			else:
				last=nums[x] 

		if temp:
			print(temp)
			print('ans:', temp[-1]-temp[0]+2)
			return temp[-1]-temp[0]+2

		else:
			print (0)
			return 0
		'''

A=Solution()
A.findUnsortedSubarray([1, 2, 3, 4])
print('=======')
A.findUnsortedSubarray([4, 1])
print('=======')
A.findUnsortedSubarray([1])
print('=======')
A.findUnsortedSubarray([2,6,4,8,10,9,15])
print('=======')
A.findUnsortedSubarray([2,6,9,5,7,17,10,13,16,30])