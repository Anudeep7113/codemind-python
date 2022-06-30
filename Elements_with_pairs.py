x=int(input())
a=list(map(int,input().split()))
for i in range(x):
    print(a[i],end=" ")
if x%2==1:
    print("0")