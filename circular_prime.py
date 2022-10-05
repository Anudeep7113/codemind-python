x=int(input())
count1=0
r=0
sum=0
i=1
count2=0
d=x
while x>0:
    r=x%10
    sum=sum*10+r
    x=x//10
for j in range(i,d+1):
    if d%j==0:
       count1=count1+1
for j in range(i,sum+1):
    if sum%j==0:
       count2=count2+1
if count1==2 and count2==2:
    print('circular prime')
elif count1==2 and count2>2:
    print('prime but not a circular prime')
else:
    print('not prime')
