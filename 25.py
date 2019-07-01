i=int(input())
a = list(map(int, input().split()))
a.sort()
n=len(a)
if(n%2!=0):
    z=(n)//2
    print(a[z])
else:
    ans=a[n//2]+a[(n-1)//2]
    j=ans/2
    print(j)
