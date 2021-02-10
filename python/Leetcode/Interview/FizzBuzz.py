class Solution:
    def fizzBuzz(self, n):
        ans=[]
        for x in range(1,n+1):
            if x % 3 == 0:
                if x % 5 == 0:
                    ans.append("FizzBuzz")
                else:
                    ans.append("Fizz")
                
            elif x % 5 == 0:
                ans.append("Buzz")
                
            else:
                ans.append(x)
                
        print(ans)
        return(ans)

A=Solution()
A.fizzBuzz(15)