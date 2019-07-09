y=int(input())
s=2**y
ys=[]
for i in range(0,s):
    l=bin(i)[2:].zfill(y)
    if(len(l)<len(bin(2**y-1)[2:])):
        ys.append([l.count("1"),l])
    else:
        ys.append([l.count("1"),l])
ys.sort()
for i in range(len(ys)):
    print(ys[i][1])
