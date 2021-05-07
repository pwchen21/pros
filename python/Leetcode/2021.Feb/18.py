class Solution:
	def numberOfArithmeticSlices(self, A):
		dis=A[1]-A[0]
		ans=0
		ct=0
		print('Init: dis ',dis, '/ans ', ans, '/ct ', 2)
		for x in range(2,len(A)):
			print('x', x)
			if dis == A[x]- A[x-1]:
				print('   1a. DIS:', A[x]- A[x-1])
				ct += 1
				print('   1b. ct', ct)
				ans = ans + ct
			else:
				print('   1c')
				dis = A[x]- A[x-1]
				ct = 0

			print('1d', ans)
		print(ans)

A=Solution()
A.numberOfArithmeticSlices([8,1,2,3,2,4,6,8])
print('=====')
A.numberOfArithmeticSlices([1,2,3,4,5,6])