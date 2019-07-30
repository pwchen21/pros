class Solution(object):
	def toHex(self, num):
		if num > 0:
			return hex(num)[2:]
		else:
			print bin(int(bin(255),2) & int(bin(num),2))
			
			#print '123'
			#print '1:', int(bin(255), 2)
			#print '2:', int(bin(abs(num)), 2)
			#print '3:', int(bin(1),2)
			
			
			#absn=abs(num)
			#com=int(bin(255)[2:])+ int(bin(absn)[2:])
			#print hex(int(com[2:]))
			
			#print com
            #return (8-len(com))*'f' + str(com)
			

A=Solution()
A.toHex(-10)