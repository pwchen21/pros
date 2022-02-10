        stack=[]
        ans=[]

        def generate(l, r):
            if l == r == n:
                ans.append(''.join(stack))
                return

            if l < n:
                stack.append('(')
                generate(l-1, r)
                stack.pop()
            if r < l:
                stack.append(")")
                generate(l, r-1)
                stack.pop()

        generate(0,0)
        return ans