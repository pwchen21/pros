def nextGreaterElement(findNums, nums):
	result=[-1]*len(findNums)
	fn=0
	for x in findNums:
		gtidx=nums.index(x)
		for y in nums[gtidx:]:
			if y > x:
				result[fn]=y
				break
		fn+=1
	print result

nextGreaterElement([], [])