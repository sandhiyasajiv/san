n=int(input(""))
sum=0
t=n
while t>0:
   d=t%10
   sum=sum+d**3
   t=t//10
if n==sum:
   print("yes")
else:
   print("no")
