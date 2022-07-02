x=input()
a="abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM"
b="0987654321"
c=0
for i in x:
    if((i not in a) and (i not in b) and i!=' '):
        c+=1
print(c)
       
 