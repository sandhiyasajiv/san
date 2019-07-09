try:
	num=int(input())
	array=list(map(int,input().split()))
	na=[]
	for i in array:
		if array.count(i)>1:
			if i not in na:
				na.append(i)
	print(*na)
	if len(na)==0:
		print("unique")
except ValueError:
	print("invalid")
