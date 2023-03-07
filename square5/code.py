S = int(input())
N = int(input())


# print the square using nested loops
for i in range(N):
    for j in range(N):
        # calculate the current number
        num = S + j
        
        # print the current number with a space
        print(num, end=" ")
    
    # move to the next row
    print()
