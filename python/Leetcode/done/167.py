def twoSum(numbers, target):
	se=sorted(set(numbers))
	print se
	for x in se:
		if target-x in numbers:
			if numbers.index(x)+1 == numbers.index(target-x)+1:
				print numbers.index(x)+1, numbers.index(target-x)+2
			else:
				print numbers.index(x)+1, numbers.index(target-x)+1

twoSum([0,0,3,4],0)
print '==='
twoSum([2,3,1,4],6)
print '==='
twoSum([-1,0],-1)
