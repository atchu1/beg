n,m,o=map(int,input().split())
x=0
for i in range(1,o+1):
  x+=n+m*(o-i)
print(x)
  
