s=input()
sum=0
for char in s:
    if char.isdigit():
        sum+=int(char)
print(sum)