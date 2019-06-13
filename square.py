import math
m,a=list(map(int,input().split()))
c=m*a
x=int(math.sqrt(c))
if(c==x*x):
  print("yes")
else:
  print("no")
