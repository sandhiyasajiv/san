num=list(input())
y=len(num)
for s in range(0,y,2):
    temp=num[s]
    num[s]=num[s+1]
    num[s+1]=temp
print("".join(num))
