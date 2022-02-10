A={"C":1, "B":2, "D":3}
print(A["C"])
A["F"]=3
print(A)

if A.get("Y"):
    print(True)
else:
    print(False)


#print(len(A))
print(len(set(A.values())))
#print(A.values())