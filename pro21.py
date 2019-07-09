y=int(input())
s=list(map(int,input().split()))
ans=int(y/2)
ys=s[:ans]
sa=s[ans::]
if ((sum(ys)//len(ys))==(sum(sa)//len(sa))):
    print("yes")
else:
    print("no")
