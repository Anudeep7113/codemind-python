def st(s):
    n=len(s)
    if s[0]=="(" and s[n-1]==")":
        print("True")
    else:
        print("False")
s=input()
st(s)