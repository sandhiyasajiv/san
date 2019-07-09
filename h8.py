num=int(input())
lst=input().split()
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        for k in range(j+1,len(lst)):
            if(int(lst[i])+int(lst[j])==int(lst[k])):
                print(lst[i],lst[j],lst[k])
