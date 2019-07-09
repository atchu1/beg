s=int(input())
a=list(map(int,input().split()))
for p in range(len(a)-1):
     if(a[p]>a[p+1]):
           print(p)
           break
