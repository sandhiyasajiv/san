a,b=input().split()
ys=abs(len(b)-len(a))
for i in range(len(a)):
    if(len(b)==1 and b[i] in a):
        break
    if (a[i]!=b[i]):
        ys=ys+1
print(ys)
