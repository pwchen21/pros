class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
		p=0
		#print 'o-flowerbed', flowerbed
		for x in range (len(flowerbed)):
			if flowerbed[x]==0:
				print 'x', x
				#print 'x==0' , x==0
				if x == 0 and (len(flowerbed)>1):
					if flowerbed[x+1]==0:
						flowerbed[x]=1
						p+=1				
					#print '1-flowerbed:',flowerbed
					print '1-p:', p
				elif x == len(flowerbed)-1 and ( len(flowerbed) >1):
					if flowerbed[x-1]==0:
						flowerbed[x]=1
						p+=1
					#print '2-flowerbed:',flowerbed
					print '2-p:', p			
				
				elif len(flowerbed) == 1:
					p+=1
					#print '0-flowerbed:',flowerbed
					print '0-p:', p	
				else:
					if flowerbed[x-1]==0 and flowerbed[x+1]==0:
						flowerbed[x] = 1
						p+=1
						#print '3-flowerbed:',flowerbed
						print '3-p:', p
				print 'flowerbed:',flowerbed
						
		if p >= n:
			print True
				
		print False
				

	
A=Solution()
A.canPlaceFlowers([0,0,1,0,0], 1)