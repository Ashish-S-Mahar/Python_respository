# x = "lower"
# print(x.upper())

# y = "HELLO"
# print(y.lower())    

# x = [57,56,246,865,244]
# # string v hota h
# print(max(x))
# print(min(x))

# to find vawels in string

# x = input("Enter the name....")
# x = "ashish"
# y = len(x)
# print(y)
# count = 0
# for i in x:
#     if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         count+=1
#         print(i)
#     else:
#         print("",end="")

# remove middle element of list....

x = [1,4,2,6,8,10]
y = int(input("Enter removing num.."))
li=[]

for i in x:
    if(i==x[y-1]):
        continue
    else:
        li.append(i)

print(li)