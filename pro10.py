num=int(input())
arr=[int(i) for i in input().split(" ")]
n1=0
for j in range(num):
      for k in range(j):
           if(arr[k]<arr[j]):
                n1+=arr[k]
print(n1)
