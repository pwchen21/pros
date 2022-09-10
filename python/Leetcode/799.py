def chamt(poured, query_row, query_glass):
    q=[poured]
    print(q)
    for r in range(query_row):
        print(r)
        q2=[0]*(len(q)+1)
        for i, amount in enumerate(q):
            print(i, amount)
            if amount <=1:
                continue
            else:
                tmp = (amount -1) /2
                q2[i] += tmp
                q2[i+1] +=tmp
        q=q2
        print(q)
    print(min(q[query_glass], 1))


chamt(30, 10, 2)