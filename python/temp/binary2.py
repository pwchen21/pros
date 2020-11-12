def solution(N):
    str_bin = bin(N)[2:]
    print(str_bin)
    save_gap = []
    gap = 0
    for value in str_bin:
        if value == "0":
            gap += 1
            print(gap)
        if gap > 0 and value == "1":       
            save_gap.append(gap)
            gap =0   
    if not save_gap:
        return 0
    else:
        return max(save_gap)
        

solution(10004)

