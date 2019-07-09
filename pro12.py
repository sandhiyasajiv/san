ys,sa = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(sa):
  yu,s = map(int, input().split())
  print(min(lst[yu-1:s]))
