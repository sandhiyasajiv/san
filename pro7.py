ys=int(input())
sa=[]
dif=0
for g in range (0,ys+1):
    dif=abs((2**g)-ys)
    sa.append(dif)
yu=min(sa)
print(yu)
