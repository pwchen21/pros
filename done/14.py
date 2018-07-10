class Solution(object):
    def longestCommonPrefix(self, strs):

		def ckstrs(strs, findstr):
			print '==call ckstrs==='
			print 'findstr', findstr
			n=0
			for x in strs:
				print 'x now:', x
				print 'Prefix now:', y
				print "pl, cl", pl, cl
				if x.find(findstr) != 0:
					return False
				elif x.find(strs[0][:pl-cl]) == 0:
					n=n+1
				if n == cstr:
					return True
			print '===end chkstrs==='
		
		if not strs:
			print "CCC"
			#return ""
			
		else:
			pl=len(strs[0]) #Current Prefix
			print 'current prefix:', pl
			cstr=len(strs) #all str
			print 'count str:', cstr
			cl=0 #length of cut
		
		for y in range(pl):
			findstr=strs[0][:pl-cl]
			if ckstrs(strs, findstr) == True:
				print 'answer:', findstr
				#return findstr
			else:
				cl+=1				
		print "AA"
	

A=Solution()
A.longestCommonPrefix(['cde','abfe', 'afferjiejri', 'cdaerer'])
#A.longestCommonPrefix([""])