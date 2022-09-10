    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        max_dep = 0
        ans = 0
        
        while q:
            cand, depth = q.pop()
            print("==")
            print(cand, depth)
            if depth > max_dep:
                ans = 0
                max_dep = depth
                print('max_dep set to:', max_dep)
            if depth == max_dep:
                ans += cand.val
                print('ans now:', ans)
            if cand.left: 
                q.append((cand.left, depth+1))
            if cand.right: 
                q.append((cand.right, depth+1))
            print('q', q)
        return ans