#  chutta dhoondo

x = int(input("Enter the amount :- "))


count2000 = 0
count500 = 0
count200 = 0
count100 = 0
count50 = 0
count20 = 0 
count10 = 0
count5 = 0
count2 = 0
count1 = 0



if(two000<= x):
    x = x // two000
    count2000 += x%2000
if(five00<= x):
    x = x // five00
    count500 += x%500 

if(two00 <= x):
    x = x // two00
    count200 += x%200

if(hun <= x):
    x = x // hun
    count100 += x % 100


if(fifty <= x):
    x = x // fifty
    count50 += x%50

if(twenty <= x):
    x = x // 20
    count20 += x % 20

if(ten <= x):
    x = x // 10
    count10 += x % 10


if(five <= x):
    x = x // 5
    count5 += x % 5

if(two <= x):
    x = x // 2
    count2 += x % 2

if(one <= x):
    x = x // 1
    count1 += x % 1


else:
    print("Enter valid amount....")

