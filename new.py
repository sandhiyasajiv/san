n=int(input())
space=n*2
for i in range(0,n):
  for j in range (0,space):
    print(" ",end='')  
  space=space-2
  for j in range(0,i+1):
    print('*',end=' ')
  print('\r')  
#print(n)
space=n*2
#print(space)
for i in range(0,n):
  for j in range (j+1,space):
    print(" ",end=' ')  
  space=space+2
  for x in range(i+1,n):
    print('*',end=' ')
  print('\r')  
