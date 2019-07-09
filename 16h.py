n,k=map(int,input().split())
array=[[abs(i1-k),i1]for i1 in [int(x1) for x1 in input().split()]]
array.sort()
array=array[1:]
array=[i1[1] for i1 in array[:3]]
print(*array)
