class Solution(object):
    def findRestaurant(self,list1, list2):
		AD={key:i for i, key in enumerate(list1)}
		#print 'AD:', AD		
		count=1000000
		ans=[]
		
		for j, k in enumerate(list2):
			i=AD.get(k,100000)
			# get default 1000000
			#print type(i)
			#print type(j)
			#print 'k', k
			#print '[i, j]', [i, j]
			if i+j < count:
				count = i+j
				ans=[k]
			elif i+j == count:
				ans.append(k)
			
		print 'Answer', ans
		#beat7.18% solution
		"""
		sum=0
		pick={}
		Ans=[]
		for x in list1:
			#print 'x:', x
			#print x in list2
			if x in list2:
				#print x
				pick[x] = list1.index(x)+ list2.index(x)
			#else:
				#print 'none'
		for x in pick.keys():
			if pick[x] == min(pick.values()):
				Ans.append(x)
				
		print Ans
		#print pick[min(pick.keys())]
		"""
res=Solution()
res.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Burger King","Tapioca Express","Shogun"])

#res.findRestaurant(["A", "B", "C"],["B", "A", "C"])