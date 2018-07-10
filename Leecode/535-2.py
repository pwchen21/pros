import string
import random

class Codec:

	def __init__(self):
		self.di={}

	def encode(self, longUrl):
		key=string.ascii_letters+string.digits
		rl=[]
		
		for x in range(6):
			r=random.choice(key)
			rl.append(r)
			
		sht="http://tinyurl.com/"+''.join(rl)
		
		self.di[sht]=longUrl
		print self.di
		print sht 
	
	def decode(self, shortUrl):
		#print 12345
		print self.di.get(sht)
		
		
A=Codec()
A.encode("https://leetcode.com/problems/design-tinyurl")