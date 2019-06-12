p=input()
p=list(p)
n=len(p)
if n%2!=0:
    c=n/2
    d=round(c)
    p[d]='*'
else:
    c=n/2
    d=round(c)
    p[d]='*'
    p[d-1]='*'
print(*p,sep="")
