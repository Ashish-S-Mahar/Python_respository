# To count vowels in file....

x = input("Enter the name....")
x = "ashish"
y = len(x)
print(y)
count = 0
for i in x:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
        print(i)
    else:
        print("",end="")
