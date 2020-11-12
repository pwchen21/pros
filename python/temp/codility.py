def solution(A):
    heading = 0       # The sum of A[0] + A[1] + ... + A[P-1]
    tailing = sum(A)  # The sum of A[P] + A[P+1] + ... + A[N-2] + A[N-1]
    print("begin tailing")
    print(tailing)
 
    for index in xrange(len(A)):
        print("befor Aindex")
        print(A[index])
        tailing -= A[index] # The sum of A[P+1] + ... + A[N-2] + A[N-1]
        print("After Aindex")
        print(A[index])
        print("=tailing now=")
        print(tailing)
        if heading == tailing:
            # A[0] + A[1] + ... + A[P-1] == A[P+1] + ... + A[N-2] + A[N-1]
            return index
            print("I need index")
            print(index)
        heading += A[index]
        print("=heading now==")
        print(heading)
    else:
        # No equilibrium is found.
        return -1
        print("No equilibrium is found.")

    
list=[-1,3,-4,5,1,-6,2,1]
solution(list)
