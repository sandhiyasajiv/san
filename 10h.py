x,y = map(int,input().split())
len2 = list(map(int,input().split()))
len3 = list(map(int,input().split()))
f =1
for i in len3:
    if i not in len2:
        print('NO')
        f = 0
        break
if(f):
    print('YES')
