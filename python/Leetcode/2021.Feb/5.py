class Solution:
	def simplifyPath(self, path):
		temp=path.split('/')
		ans=[]
		print('0', temp)
		for x in temp:
			print('1', x)
			if x in ["", "."]:
				continue
			elif x == "..":
				if ans:
					ans.pop()
			else:
				ans.append(x)
			print(ans)
		return '/'+'/'.join(ans)


A=Solution()
A.simplifyPath("/a/./b//../d//../c/")