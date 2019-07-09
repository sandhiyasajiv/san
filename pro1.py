num=int(input())
p=[]
for x in range(0,num):
 la=input()
 p.append(la)
new=[]
for x in zip(*p):
 if(x.count(x[0])==len(x)):
  new.append(x[0])
 else:
  break
print(''.join(new))
