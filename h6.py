n=input()
flag=0
a=[int(k) for k in input().split()]
for i in a:
    if(a.count(i)!=1):
        flag=1
        break
if(flag==1):
    print(i)
else:
    print("unique")
