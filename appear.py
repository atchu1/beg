a=int(input())
s=input().split()
for i in s:
    if s.count(i)==1:
        print(i)
        break
