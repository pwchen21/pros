class Solution:
	def numUniqueEmails(self, emails):
		rs=[]
		for mail in emails:
			ds=mail.split('@')[1]
			ln=mail.split('@')[0]
			if '+' in ln:
				lned=ln.split('+')[0]
				ln=lned
			if '.' in ln:
				lned=''.join(ln.split('.'))
						
			fm=lned+'@'+ds
			#print('1:'+ fm)
						
			if fm not in rs:
				rs.append(fm)
	
		return rs
				

A=Solution()
im=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
A.numUniqueEmails(im)