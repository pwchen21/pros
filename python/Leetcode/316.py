class Solution:
    def removeDuplicateLetters(self, s):
        last_occ = {}
        stack = []
        
        for i in range(len(s)):
            last_occ[s[i]] = i

        print(last_occ)

        for i in range(len(s)):
            if s[i] not in stack:
                print('1.', s[i], stack)
                while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
                    stack.pop()

                stack.append(s[i])
                
            print(stack)
        return ''.join(stack)
        
        """ #python leetcode solution
        print('stirng:', s)
        st_set=sorted(set(s))
        print(st_set)
        for x in st_set:
            print('x in set:', x)
            suffix=s[s.index(x):]
            print(suffix)
            if len(set(suffix)) == len(st_set):
                print(x + self.removeDuplicateLetters(suffix.replace(x, "")))
                return x + self.removeDuplicateLetters(suffix.replace(x, ""))
        return ""
        """
        """ #Failed Method 2
        ss=sorted(set(s))
        dic={}
        dic2={}
        ans=""
        mn=-1
        for x in range(len(s)):
            if s[x] in dic:
                dic[s[x]].append(x)
            else:
                dic[s[x]] = [x]

        print(dic)

        for y in ss:
            for t in dic[y]:
                if t > mn:
                    dic2[y]=t
                    mn=t
                    break
            if y not in dic2:
                dic2[y]=dic[y][-1]
        
        print(dic2)
                
        for j in range(len(dic2)):
            ans+=min(dic2.keys(), key=(lambda x:dic2[x]))
            dic2.pop(ans[-1])

        print(ans)
    """
    """ # Fail Method 1
        dup={}
        res=""
        for x in s:
            print("====")
            print(x)
            if x not in dup:
                dup[x] = 1
                res+=x
                print("1:", res, dup)
            elif dup[x] == 1:
                dup[x]+=1
                res=res.replace(x, "")
                res+=x
                print("2:", res, dup)
            else:
                print("3:", res, dup)
                continue
                
        print(res)
        return res
    """

A=Solution()
A.removeDuplicateLetters("cbacdcbc")
