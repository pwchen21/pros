# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    # write your code in Python 2.7

    def doso(A,K):
        rotalist=[]
        listaf=A[K-1:]
        print("==listaf==")
        print(listaf)
        listbe=A[:K-1]
        print("==listbe==")
        print(listbe)
        for afva in listaf:
            rotalist.append(afva)
        for beva in listbe:
            rotalist.append(beva)
        print("final result is call doso")
        print rotalist
        print(type(rotalist))
        return rotalist
    pass
    
    listl=len(A)
    print("=listl=")
    print(listl)
    if K == listl-1:
        K=listl
        print("4")
        print(A)
        return A
    if K > listl-1:
        temp=str(K)
        x=temp[0]
        #for x in str(K):
        print("x=")
        print(x)
        print(type(x))
        ik=int(x)
        print(type(ik))
        print(ik)
        print(listl-1)
        if ik<=listl-1:
            print("==test==")
            K=ik
            print(A,K)
            print("11")
            doso(A,K)
            
        if x == 0:
            print("22")
            print(A)
            return A
    if K ==0:
        print("3")
        print(A)
        return A

    else:
        print("else")
        doso(A,K)
    
    
    pass

print("pro1")
solution([0,-9], 2)
print("pro2")
solution([0,-9], 1)
print("pro3")
solution([1, 1, 2, 3, 5], 42)
print("pro4")
solution([3,8,9,7,6],3)
