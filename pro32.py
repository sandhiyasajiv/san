y,s=map(int,input().split())
if y>s:
    y,s=s,y
lst=[]
for i in range(y):
    lst2=list(map(int,input().split()))
    lst2.sort()
    lst.append(lst2)
for j in range(0,s):
    lst3=[]
    for i in range(0,s):
        lst3.append(lst[i][j])
    lst3.sort()
    x=0
    for i in range(0,y):
        lst[i][j]=lst3[x]
        x=x+1
for i in lst:
    print(*i)
