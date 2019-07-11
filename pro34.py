y,s=map(int,input().split())
n=0
Lst=[]
for i in range(y):
      Lst.append(input())
for j in range(y):
      for y in range(s-1):
            if(Lst[j][y]!='R' and Lst[j][y+1]!='R'):
                  n=n+3
            elif(Lst[j][y]!='G' and Lst[j][y+1]!='G'):
                  n=n+5
print(n)
