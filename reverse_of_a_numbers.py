N=int(input(""))
sum=0
while(N>0):
    r=N%10
    sum=sum*10+r
    N=N//10
print(sum)