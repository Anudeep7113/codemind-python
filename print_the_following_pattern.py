x=int(input())
a=1
for i in range(1,x+1):
    for j in range(1,i+1):
        print(a,end="")
        a=a+1
    a=1
    print()