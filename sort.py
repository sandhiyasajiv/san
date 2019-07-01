n=int(input())
o=list(map(int,input().split()[:n]))
for i in range(len(o)):
    for j in range(i+1,len(o)):
        if o[i]>o[j]:
            o[i],o[j]=o[j],o[i]
for a in range(len(o)):
    print(o[a],end=" ")
