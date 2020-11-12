def solution(N):
    str_bin = bin(N)[2:]
    save_gap = []
    gaps = 0
    gap = 0
    for value in str_bin:
        #print("for")
        if value == "0":
            gap += 1
            print(gap)
        if gap > 0 and value == "1":
            gaps += 1
            save_gap.append(gap)
            gap =0
            print("==save_gap=")
            print(save_gap)
    print("==max_gap=")
    print(max(save_gap))
    
	if not save_gap:
		print("==if not save gap==")
		return 0
		print("0")
   else:
		return max(save_gap)
		a=max(save_gap)
		print("=else=")
		print(a)


solution(10004)
