def solution(N):
    # write your code in Python 2.7
    A=list(bin(N))
    print("===A===")
    print(A)
    A.reverse()
    A.pop()
    A.pop()
    A.reverse()
    print("===A===")
    print(A)
    find_max=0
    lag=[]
    j=0
    for x in A:
        print("=x=")
        print(x)
        if x == '0':
            j=j+1
            print("==j==")
            print(j)
        elif x == '1':
            lag.append(j)  
            j=0
            print("=lag=")
            print(lag)
    for y in lag:
        print("=y=")
        print(y)
        if y >= find_max:
            find_max=y
            print("=y=")
            print(y)
    print(find_max)
    return find_max
    pass

solution(1024)
