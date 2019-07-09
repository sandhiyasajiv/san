num=input()
flag=0
array=[int(k) for k in input().split()]
for i in array:
    if(array.count(i)!=1):
        f=1
        break
if(f==1):
    print(i)
else:
    print("unique")
