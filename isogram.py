z=input()
z=list(z)
a=0
for i in z:
      if(z.count(i)==2):
          a=a+1
if(a==0):
     print("Yes")
else:
     print("No")
