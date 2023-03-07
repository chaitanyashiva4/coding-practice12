a=input()
b=input()
res=""
for i in range(len(a)):
    if i%2==0:
        f=a[i]
        res+=f 
    else:
        f=b[i]
        res+=f 
print(res)
