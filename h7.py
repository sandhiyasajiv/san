num=int(input())
lst=input().split()
for it in range(0,len(lst)):
    if(it%2==0):
        if(int(lst[it])%2==1):
            print(lst[it],end=' ')
    else:
        if(int(lst[it])%2==0):
            print(lst[it],end=' ')
