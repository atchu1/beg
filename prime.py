x=int(input())
if x> 1:  
   for i1 in range(2, x): 
       if (x % i1) == 0: 
           print("no") 
           break
   else: 
       print("yes") 
else: 
   print("no") 
