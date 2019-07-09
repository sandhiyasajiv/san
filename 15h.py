num=int(input())
array=list(map(int,input().split()))
C=0
b=[]
d=[]
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if array[i]<array[j]:
            C=C+1
            break
    else:
        b.append(array[i])        
print(*b)
print(max(array))
