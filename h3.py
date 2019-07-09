num=int(input())
lst=input().split(" ")
lst=[int(num) for num in lst]
final=[]
for x in range(0,num):
  if(x==lst[x]):
    final.append(lst[x])
if not(len(final)==0):
  final=sorted(final)
  for i in range(0,len(final)):
    print(final[i],end=' ')
else:
  print("-1")
