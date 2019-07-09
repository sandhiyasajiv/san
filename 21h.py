n,k=map(int,input().split())
ar=[]
l1=[]
for i in range(n):
    l=[int(ar) for ar in input().split()]
    ar.append(l)
    if 0 in l:
        m=l.index(0)
        l1.append(m)
for i in range(len(ar)):
    if 0 in ar[i]:
        for j in range(k):
            ar[i][j]=0
for i in l1:
    for j in range(n):
        ar[j][i]=0
for i in ar:
    print(*i)
