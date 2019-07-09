try:
	n=int(input())
	array=list(map(int,input().split()))
	for it in array:
		if array.count(it)==1:
			print(it)
except ValueError:
	print("invalid")
