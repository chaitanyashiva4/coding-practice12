n=int(input())
k=1 
j=0 
k=2*n-1 
for i in range(1,n+1):
    left="  "*(j)
    print(left+"* "*k)
    k=k-2 
    j=j+2
    
