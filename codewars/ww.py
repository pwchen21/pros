def hwt(wts):
    wtsl=wts.split(" ")
    res=[]
    dic={}
    print("P0:", wts)
    ind=0
    for x in wts:
        print("P1:", x, wwt(x))
        dic[ind][0][0] = x
        dic[ind][0][1] = wwt(x)
        ind+=1
    print(dic)
        
def wwt(vlu):
    wwvlu=0
    for x in range(len(vlu)):
        wwvlu+=int(vlu[x])    
    print(wwvlu)
    return(wwvlu)
    
hwt("70 50 90 80 30")