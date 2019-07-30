def hwt(wts):
    wtsl=wts.split(" ")
    tmp=[]
    res=[]
    res1=''
    dic={}   
    #print("P0:", wtsl)
    ind=0
    for x in wtsl:
        #print("P1:", x)
        dic[ind] = [x, wwt(x)]
        ind+=1
        #print("P2:", wwt(x))
    print(dic)
    
    #Sort by weight value
    for x in dic:
        tmp.append(dic[x][1])
        #print('tmp:', tmp)
    
    tmp1=sorted(set(tmp), reverse=False)
    print(tmp)
    print(tmp1)
    
    for x in tmp1:
        print('x:', x)
        if tmp.count(x) > 1:
            dup=[]
            for y in dic:
                if dic[y][1]==x:
                    dup.append(dic[y][0])
            print('dup', dup)
            
            for z in sorted(dup):
                res.append(z)
            
        else:
            for y in dic:
                if dic[y][1]==x:
                    res.append(dic[y][0])
    
    
        
    print(' '.join(res))
    
 
def wwt(vlu):
    wwvlu=0
    #print('P3:', len(vlu))
    for x in range(len(vlu)):
        wwvlu+=int(vlu[x])    
    #print(wwvlu)
    return(wwvlu)
    
hwt("2000 10003 1234000 44444444 9999 11 11 22 123")