n=int(input("enter"))
for i in range (n):
    for j in range (n-i): 
        print("*",end=" ")
    print()
for k in range (n):
    for b in range (k+1):
        print("*",end=" ")
    print()