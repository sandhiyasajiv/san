y,s=map(int,input().split())
if y>s:
    y,s=s,y
lst=[]
for i in range(y):
    lst1=list(map(int,input().split()))
    lst1.sort()
    lst.append(lst1)
for j in range(0,s):
    lst2=[]
    for i in range(0,y):
        lst2.append(lst[i][j])
    lst2.sort()
    x=0
    for i in range(0,y):
        lst[i][j]=lst2[x]
        x=x+1
for i in lst:
    print(*i)
