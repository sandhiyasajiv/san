n=int(input())
lst=list(map(int,input().split()))
re=1
len=[]
for i in lst:
  re=re*i
for i in lst:
  len.append(re//i)
print(*len)
