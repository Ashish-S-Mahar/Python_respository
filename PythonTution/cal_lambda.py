# It is a calculator made by lambda function asking the numbers again and again....

while(True):
    x = int(input("Enter the 1st num..."))
    y = int(input("Enter the 2nd num..."))
    z = input("Enter the symbol...")
    if(z=="+"):
        add = lambda x,y:x+y
        print(add(x,y))
    elif(z=="-"):    
        sub = lambda x,y:x-y
        print(sub(x,y))
    elif(z=="/"):
        div = lambda x,y:x/y
        print(div(x,y))
    elif(z=="*"):
        mul = lambda x,y:x*y
        print(mul(x,y))
    else:
        print("Please enter the right operator...")
        break