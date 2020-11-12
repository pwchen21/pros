def intersection(nums1, nums2):
	sn1=set(nums1)
	sn2=set(nums2)
	res=[]
	for x in sn1:
		if x in sn2:
			res.append(x)
			
	print res

intersection([1,2,2,1], [2,2])