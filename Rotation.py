n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    for j in range(b):
        k=c.pop()
        c.insert(0,k)
    print(*c)