def rank(gamers, wgt, rank):
    gm_ls = gamers.split(',')
    gw_dic = {}
    gm_ss = []
    idx=0
    print("1:", gm_ls, wgt, rank)
    if gamers:
        if len(gm_ls) > rank-1:
            for gamer in gm_ls:
                gw_dic[gamer]=(len(gamer)+ gmrc(gamer)) * wgt[gm_ls.index(gamer)]
                print("2:", gamer, ":", len(gamer), "+" , gmrc(gamer), "wt:" , wgt[gm_ls.index(gamer)], 'Res:', gw_dic[gamer])               
            print("3:", gw_dic)
            sort_pre=sorted(gw_dic.values(), reverse=True)
            sort_dictvalu=sort_pre[rank-1]
            print("4:" , sorted(gw_dic.values(), reverse=True))
            #print("5:" , sorted(gw_dic.values())[rank-1])
            idx=sort_pre.index(sort_dictvalu)
            print("5-1:", idx)
            #Check if the gamer get the same score
            for gamer in gw_dic:
                if gw_dic[gamer] == sort_dictvalu:
                    print("6-0", gamer,":", sort_dictvalu)
                    gm_ss.append(gamer)
                
            
            gs=sorted(gm_ss)
            print("6:", gs)
           
            if idx + 1 != rank:
                print('x:', idx+1-rank)
                print(gs[rank-idx-1])
                return gs[rank-idx-1] 
            else:
                print(gs[0])
                return gs[0]
            """
            if len(gm_ss) != 1:
                if len(gm_ss) > rank:
                    rank = len(gm_ss)
                print("7:",sorted(gm_ss)[rank-1])
                return sorted(gm_ss)[rank-1]
            else:
                return gm_ss[0]
            """
        else:
            print("Not enough participants")
            return "Not enough participants"
    else:
        print("No participants")
        return "No participants"
           
def gmrc(name):
    sum=0
    for alp in name:
        sum += ord(alp.lower()) - 96
    return sum

    
print("==1==")	
rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)

print("==2==")
rank("Lagon,Lily", [1, 5], 2)

print("==3==")
rank("", [4, 2, 1, 4, 3, 1, 2], 6)

print("==4==")
rank("Bmn,Ann", [2,2], 1)

print("==5==")
rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden",[1, 3, 5, 5, 3, 6],2)

print("==6==")
rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth" ,[3, 1, 4, 4, 3, 2],4)

print("==7==")
rank("Aubrey,Olivai,Cheol,Abigail,Chloe,Andrew,Elizabeth" ,[3, 1, 4, 4, 4, 3, 2],5)
