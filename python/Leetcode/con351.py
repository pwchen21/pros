class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
		plant = 0
		print flowerbed
		print 'len(flowerbed)', len(flowerbed)
		for x in range (0, len(flowerbed)-1, 1):
			print 'x', flowerbed[x]
			if flowerbed[x] == 1:
				space = 0
			else :
				if flowerbed[x+1] == 1:
					space = 0
					print 'set s=0'
				else:
					space = 1
					print 'set s=1'
			if flowerbed[x] == 0 and space == 1:
				plant +=1
				space = 0
				print 'plant+1'
			print '--round--'
		print 'final plant', plant
		if plant > n:
			print True
		else:
			print False

        

TestBed=Solution()
TestBed.canPlaceFlowers([1,0,0,0,1], 1)
print '===='
TestBed.canPlaceFlowers([1,0,0,0,0,1], 2)