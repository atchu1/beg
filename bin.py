num=input("")
d=0
for i in range(len(num)):
  if(num[i]!="0" and num[i]!="1" ):
    d=d+1
if(d>=1):
  print("no")
elif(d==0):
  print("yes")      
         
    
