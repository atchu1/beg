import math
m,a=list(map(int,input().split()))
s=math.gcd(m,a)
print((m*a)//s)
