a,b=input().split()
y=abs(len(b)-len(a))
for i in range(len(a)):
    if(len(b)==1 and b[i] in a):
        break
    if (a[i]!=b[i]):
        y=y+1
print(y)
