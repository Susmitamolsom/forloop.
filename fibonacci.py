a=0
b=1
c=0
print(a,b,end=" ")
for i in range (1,11):
    c=a+b
    a=b
    b=c
    print(c,end=" ")