import random #for F4
import secrets
import collections #for B5
from itertools import combinations #for F5
from collections import defaultdict
import math


print(7%3)
print(6/3)
# for x in range(10):
#    print(x)

# D={"a":1, "b":2, "c":3}
# for (k, v) in D.items(): 
#     if "a" in D.keys():
#         print('yes')
#     #if D.has_key('a'): #py 2.7 function
#     #    print('aa')


# print("====B0. String Test====")
# t="abcde"
# #t.del("c")
# #print(t)
# print(set(t))
# print(''.join(sorted(set(t))))

# print("S0:", [x for x in t])

# s='0000001011'
# ist=(int(s, 2))
# print(ist)

# print("\n====B1. List Test====")
a=[1,2,3,4,5]
print('here:', a.index(4))
print('tt:', a[-1])
# for x in range(len(a)):
#     print(x)

# a=[1,2]
# print(sorted(a))
# print(a[-3:])
# print(a)
# print('h:', a)
# print(a.sort(), a)
# print('hhhh:', a.index(2, a.index(2)))

# A=[1,2,3,3, 5, 6, 4]
# A.remove(3)
# print('remove', A)
# del A[1]
# print('delete:', A)

# A[3:]=sorted(A[3:])
# print(A)

# #del a[2]
# print(a)
# c=[1,2,3,4,1,5]
# #print(diff(a,c))
# b=['a', "b", "c", "d", "e"]
# b.reverse()
# print(b)

# d=[]
# print(not d)



# print("\n====B2. Dictionary Test====")
# D={"a":[], "b":2, "c":3}
# if "a" in D: 
#     print('y')
# print(D)

# D["a"].append('x')
# D["a"].append('c')
# print(D)
# #print(D['d'])

# ans = defaultdict(str)
# print(ans)
# ans[0]='x'
# print(ans)

# ans1 = defaultdict(list)
# print(ans1)
# ans1[0].append('x')
# ans1[0].append('y')
# print(ans1)


# t="abc"
# D[t] = 9
# print(D)
# print("a" in D)
# print()

# D["d"] = 4
# print("aa", D)

# dic={"a":[0,1,2], "b":[2,3,4], "c":[4,5,6]}
# dic["d"]=[0]
# dic["d"].append(1)
# print(dic)

# print("\n====B4. Number Operation====")
# print(10^-4)


# print("\n====B5. Hash Map====")
# check_in = {}
# check_in["0001"] = ("Taipei", 8)
# print(check_in)
# counter= collections.defaultdict(int)
# stations = collections.defaultdict(int)
# print(stations)
# temp = check_in.pop("0001")
# print(temp)
# stations[temp[0], temp[1]] = 10
# counter[temp[0], temp[1]] = 1
# print(stations)
# print(counter)

# print("\n====B5. ior====")

# d1 = {"a": 0, "b": 1, "c": 2}
# d2 = {"c": 20, "d": 30}

# d1 |= d2
# print(d1)

# print("\n====F0. Enumerate====")
# s="jiijiadfa"
# li={}
# for i, c in enumerate(s):
#     print(i, c)
#     li[c]=i


# print("\n====F1. Zip====")
# print(a, b)
# for x, y in zip(a,b):
#     print(x, y)

# print("\n====F2. lambda for sort====")
# nums=[1,2,1,0,2,4,12,0]
# nums.sort(key=lambda x: 1 if x==0 else 0 )
# print(nums)

# print("\n====F3. Range====")
for x in range(10, 0, -1):
     print(x)

# print("\n====F4. Random====")
# print(secrets.token_hex(2))
# print(secrets.token_urlsafe(2))  # require bit + 1

# print(random.randint(1, 10))  # random from 1 to 10
# print(random.getrandbits(10))


# print("\n====F5. Random====")
# ans = []
# for comb in combinations(range(1,10), 3):  #在1~10中找出三個值
#     if sum(comb) == 7:  #總合為7
#         ans.append(comb)
# print(ans)

# print("\n====F6. Print All posible combinations====")
#return list(set(permutations(nums))) # 列出所有可能的排列組合
  
    # def fizzBuzz(self, n):
    #     ans = []

    #     for num in range(1,n+1):
    #         if num % 3 == 0 and num % 5 == 0:
    #             ans.append("FizzBuzz")
    #         elif num % 3 == 0:
    #             ans.append("Fizz")
    #         elif num % 5 == 0:
    #             ans.append("Buzz")
    #         else:
    #             ans.append(str(num))

    #     return ans

#a, b = 20, 100
#print('h', math.gcd(a,b))
print(1 & 2)


# from timeit import Timer
# D = dict((x, y) for x, y in zip(range(1000), range(1000)))
# from timeit import Timer 
# t = Timer("D.has_key(500)", "from __main__ import D")
# t.timeit()
# t = Timer("500 in D", "from __main__ import D")
# t.timeit()  