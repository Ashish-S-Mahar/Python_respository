# Its a "Fibonacci series" made by "if,else"condition...

x = 0
y = 1
z = int(input("Enter the value..."))

if(z==0):
    print("Enter value...")
elif(z==1):
    print(x)
elif(z==2):
    print(x)
    print(y)
else:
    print(x)
    print(y)
    for i in range(1,z-1):
        a = x+y
        x=y
        y=a
        print(a) 
