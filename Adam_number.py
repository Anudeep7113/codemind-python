x=int(input())
sq=x*x
r=0
sum=0
r1=0
sum1=0
while x>0:
    r=x%10
    sum=sum*10+r
    x=x//10
sq1=sum*sum
while sq1>0:
    r1=sq1%10
    sum1=sum1*10+r1
    sq1=sq1//10
if sq==sum1:
    print(True)
else:
    print(False)