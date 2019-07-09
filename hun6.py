num=int(input())
array=list(map(int,input().split()))
for i in array:
  if array.count(i)>1:
      print(i)
      break
  else:
      print("unique")
      break
