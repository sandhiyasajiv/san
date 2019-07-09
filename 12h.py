x,y=input().split()
num1=int(x)
num2=int(y)
lst1=list(map(int,input().split()))
lst2=sorted(lst1)
e=lst2[::-1]
print(e[num2-1])
