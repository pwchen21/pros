def majorityElement(nums):
	res=[]
	snums=set(nums)
	for x in snums:
		if nums.count(x) > len(nums)/2:
			res.append(x)
	print res

majorityElement([3,4,2,2,2,2,1,2])