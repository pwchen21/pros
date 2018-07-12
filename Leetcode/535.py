import string
import random

class Codec:
	#di={}
	def encode(self, longUrl):
		key=string.ascii_letters+string.digits
		#print key
		rl=[]

		for x in range(6):
			r=random.choice(key)
			rl.append(r)
			#print rl		
		
		sht="http://tinyurl.com/"+''.join(rl)
		print sht
		#di[sht]=longUrl
		#print di 
		
    def decode(self, shortUrl):
		#print "decode"
		di.get(shortUrl)

A=Codec()
A.encode("https://leetcode.com/problems/design-tinyurl")
A.decode("http://tinyurl.com/4Et51A")

