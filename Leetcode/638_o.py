class Solution(object):
	def shoppingOffers(self, price, special, needs):
		#Count Original Price
		og=0
		for x in range(len(price)):
			og+= price[x] * needs[x]		
		
		print 'Price without special:', og
		
		self.price=price
		self.special=special
		self.cur=needs
		#print 'Minium Price', min(og, self.getCombSpecial(needs))
		return min(og, self.getCombSpecial(needs))
		
	#Check for special price
	def getCombSpecial(self , needs):
		print 'Price:' , self.price
		print 'Special: ', self.special
		print 'Current Need: ', self.cur
		
		for spe in self.special: #[1,1,0,4]
			#print len(cur)
			print 'spe', spe
			cur=needs
			print 'cur', cur
			
			temp=True			
			#check special big then current need
			for x in range(len(cur)): # cur[n,n,n]
				print 'x', x
				print 'cur[x]', cur[x]
				print 'spe[x]', spe[x]
				if cur[x] < spe[x]:
					temp=False
					print "=====False===="
					break
			# if special is ok for need
			if temp == True:
				for x in range(len(cur)):
					cur[x] = cur[x] - spe[x]
					self.getCombSpecial(cur)
				
				'''
				if cur[x] > spe[x]  # if need < spe 
					break
					#return cur[x]*price[x]
				else:
					cur[x]=cur[x]-spe[x] # if need > spe							
					#getCombSpecial(price, special, cur)
					cur= cur[x] - spe[x] # current need
					print 'current need', cur
				'''
		return 4 # Return min with special price
		
		
	
A=Solution()
A.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1])