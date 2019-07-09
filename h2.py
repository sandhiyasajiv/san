num=int(input())
lst=list(map(int,input().split()))
lst.sort()
lst.reverse()
if lst[0]==0:
    print(0)
else:
    for i in lst:
        print(i,end='')
