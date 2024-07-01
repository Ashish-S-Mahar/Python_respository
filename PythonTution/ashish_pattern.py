x = int(input("Enter the value..."))
for i in range(1,x+1):
    for j in range(1,x+1):
        if(i==1 or i==x or j==1 or j==x):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x+1):
        if(i==1 or i==x or j==1):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x+1):
        if(i==x or j==1 or j==x):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x-3):
        if(j==1):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x+1):
        if(i==1 or i==x or j==1):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x+1):
        if(i==x or j==1 or j==x):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    print()
for i in range(1,x+1):
    for j in range(1,x+1):
        if( j==1 or j==x):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x+1):
        if(i==x or j==x):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x+1):
        if(j==1 or j==x):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x-3):
        if(j==1):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x+1):
        if(i==x or j==x):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    for j in range(1,x+1):
        if(j==1 or j==x):
            print("x",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,x-2):
            print(" ",end=" ")
    print()
print()
