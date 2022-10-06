x=int(input())
a=list(map(int,input().split()))
a=sorted(set(a))
l=len(a)
if x==2:
    print(max(a))
else:
    print(a[l-3])