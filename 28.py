n=int(input())
ls=list(map(int,input().split()[:n]))
for i in range(n):
  print(ls[i],i)
