# its a normal calculator made by while function ,.............,


x = int(input("Enter the 1st number:-"))

sign = input("Enter the operator:-")

y = int(input("Enter the 2nd number:-"))



if(sign=="+"):
    print(x+y)

elif(sign=="-"):
    print(x-y)

elif(sign=="*"):
    print(x*y)

elif(sign=="/"):
    print(x/y)

else:
    print("The operator is invalid.......")