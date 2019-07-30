def count_sheep(n):
    res=[]
    for x in range(1,n+1,1):
        res.append(str(x))
        res.append(" sheep...")
        
    print(res)
    print(''.join(res))

count_sheep(10)