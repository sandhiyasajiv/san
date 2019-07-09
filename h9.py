num=int(input(""))
array=list(map(int,input().split()))
length=len(array)
large=max(array)
y,z=0,0
for i in range(0,length-1):
 for j in range(i+1,length):
  if abs(array[i]+array[j])< large:
   y,z=array[i],array[j]
   large=abs(y+z)
print(y, z)
