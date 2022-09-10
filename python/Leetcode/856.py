class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] #The score of the current frame
        for x in s:
            print(x)
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

            print(stack)


        return stack.pop()

A=Solution()
A.scoreOfParentheses("((())())")