n=int(input("enter"))
for i in range (n):
    for j in range (n):
        if j==0 or i==0 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()