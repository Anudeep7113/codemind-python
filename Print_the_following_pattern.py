x=int(input())
a=1
for i in range(1,x+1):
    for j in range(i,x+1):
        print(a,end=" ")
        a=a+1
    print()
    a=i+1