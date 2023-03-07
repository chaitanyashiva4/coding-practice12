n=(input())
res=0
for i in n:
    if int(i)%2==0:
        res+=1 
if res>2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
