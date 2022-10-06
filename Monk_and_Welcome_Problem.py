x=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(x):
    c=a[i]+b[i]
    print(c,end=" ")


