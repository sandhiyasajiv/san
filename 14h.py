def toString(list):
    return ''.join(list)
def per(a,l,r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            per(a,l+1,r)
            a[l],a[i]=a[i],a[l]
str=input()
num=len(str)
ab=list(str)
per(ab,0,num-1)
