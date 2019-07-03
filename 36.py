st=input()
count=0
for i in range(len(st)):
 if(st[i].isdigit() or st[i].isalpha() or st[i]==(" ")):
  continue
 else:
  count+=1
print(count)
