n=int(input("enter"))
for i in range (n):
    for j in range (n-i-1):
        print(" ",end=" ")
    for k in range (i+1):
        print(j+1,end=" ")
    for b in range (i,-0,-1):
        print(j,end=" ")
    print()