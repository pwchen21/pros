def findRelativeRanks(nums):
	res=[]
	sl=sorted(nums, reverse=True)
	print sl
	ti=["Gold Medal", "Silver Medal", "Bronze Medal"]
	for x in range(4,len(nums)+1):
		ti.append(str(x))
	print ti
	dictS={sl[n]:ti[n] for n in range(len(sl))}
	
	for y in nums:
		res.append(dictS.get(y))
	
	print res
	'''
	sl=sorted(nums, reverse=True)
	res=[]
	if len(nums) == 1:
		res.append("Gold Medal")
	if len(nums) == 2:
		if x == sl[0]:
			res.append("Gold Medal")
		if x == sl[1]:
			res.append("Silver Medal")
	if len(nums) >=3:
		for x in nums:
			if x == sl[0]:
				res.append("Gold Medal")
			if x == sl[1]:
				res.append("Silver Medal")
			if x == sl[2]:
				res.append("Bronze Medal")	
			if x != sl[0] and x != sl[1] and x != sl[2]:
				res.append(str(sl.index(x)+1))
		print res
	'''	
findRelativeRanks([5, 3,4, 2, 1])