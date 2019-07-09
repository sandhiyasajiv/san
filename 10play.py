ys=input()
ys=ys.split()
sa=ys[0]
y=ys[1]
count=0
i=0
while(i<len(sa) and count<2):
    if(sa[i]!=y[i]):
        count+=1
    i+=1
if(count==1 or count==0):
    print("yes")
else:
    print("no")
