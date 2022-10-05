x=int(input())
a=x
c=0
while x>0:
    c=c+1
    x=x//10
s=a*a
sum=0
r=0
r1=0
sum1=0
while c>0:
    r=s%10
    sum=sum*10+r
    c=c-1
    s=s//10
while sum>0:
    r1=sum%10
    sum1=sum1*10+r1
    sum=sum//10
if a==sum1:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')