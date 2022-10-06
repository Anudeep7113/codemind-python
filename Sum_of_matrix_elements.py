r=int(input())
c=int(input())
s=0
for i in range(r):
    a=list(map(int,input().split()))
    for j in a:
        s+=j
print(s)