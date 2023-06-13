n=int(input("enter"))
for i in range (n):
    for j in range (n-i-1):
        print(" ",end=" ")
    for b in range (2*i+1):
        print("*",end=" ")
    print()
for k in range (n-i,0,-1):
    for l in range (1,n-i+1):
        print(" ",end=" ")
    for m in range (5,2*i):
        print("*",end=" ")
    print()