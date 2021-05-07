class Solution:
    def brokenCalc(self, x, y):
    	ans=0
    	if x > y:
    		print('1ans:', x-1)
    		return(x)
    	elif x==y:
    		print('2ans', 0)
    		return 0
    	else:
    		while y > x:
    			print(x, y)
    			if y % 2 == 0:
    				ans +=1
    				y = y // 2
    			else:
    				ans +=1
    				y = y + 1


    	print('ans:', ans + x - y )


A=Solution()
print('--Q1--')
A.brokenCalc(10, 1)
print('--Q2--')
A.brokenCalc(5, 8)
print('--Q3--')
A.brokenCalc(3, 10)
print('--Q4--')
A.brokenCalc(2, 3)