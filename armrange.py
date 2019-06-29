n=int(input(""))
k=int(input(""))
for x in range(n, k + 1):
   o = len(str(x))  
   sum = 0
   t=x
   while t>0:
       digit = t%10
       sum=sum+digit**o
       t=t//10
   if x == sum:
       print(x)
