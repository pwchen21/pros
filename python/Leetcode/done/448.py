def findDisappearedNumbers(nums):
	olen=len(nums)
	nums=set(nums)
	print 'nums',nums
	start=0
	result=[]
	
	for x in range(1,olen+1):
		if x not in nums:
			result.append(x)
	print result
	
findDisappearedNumbers([4,3,2,7,8,2,3,1])
findDisappearedNumbers([1,1])
#findDisappearedNumbers([2,4,5,7,6,8])