# Checking for a Armstrong number
x=int(input("Enter the value:-"))
s=x
count=0
while(x!=0):
    r=x%10
    x=x//10
    count=count+r**3
if(s==count):
    print("its a Armstrong number")
else:
    print("its Not an armstrong number")



# k = int(input("Enter the value: "))
# def arm(a):
#     x = a 
#     count=0
#     s=x
#     while(x!=0):
#         r=x%10
#         x=x//10
#         count=count+r**3
#     if(s==count):
#         print(a,"is Armstrong number....")
# for i in range(1,k+1):
#     arm(i)

