ys=input()
x=0
for i in range(0,len(ys)-1):
  for j in range(i+1,len(ys)):
    if ys[i]<ys[j]:
      x=1
      print(ys[j:])
      break
  if x==1:
    break
else:
  print(ys)
