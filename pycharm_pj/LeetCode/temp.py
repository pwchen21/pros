a=[1,2,3,4,5,6]
print(len(a)/2)
'''
for x in a[:]:
    print(x)
    print(a)
    if x == 2:
        a[2] ='x'

'''
print(sorted(a, reverse= True) )
print(a)