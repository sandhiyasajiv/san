from itertools import combinations
ys,p=list(input().split())
k=[]
p=int(p)
length=combinations(ys,len(ys)-p)
for i in length:
  k.append("".join(i))
print(min(k))
