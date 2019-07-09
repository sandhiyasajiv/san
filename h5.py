num=list(map(str,input()))
set=cs=0
for i in range(0,len(num)-1):
  q=num[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+num[j]
    if int(q)<27 and int(q)>0: set=set+1
    elif int(q)==0: set=set-1
    else: break
if set!=1: cs=set%2
print(set+cs+1)
