num=input()
f=0
array=[int(k) for k in input().split()]
for i in array:
    if(array.count(i)!=1):
        fl=1
        break
if(fl==1):
    print(i)
else:
    print("unique")
