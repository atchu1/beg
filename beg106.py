n,m=map(int,input().split())
a=input().split()
s=[]
for i in a:
  if int(i)%2!=0:
     s.append(i)
print(s[m-1])
