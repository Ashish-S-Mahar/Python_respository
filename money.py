#  Its a file in which we count change money.....

x = int(input("Enter total Amount :-     "))

rs1 = 0             # For adding total money.... 

rs2 = 0             # For adding total money.... 

rs5 = 0             # For adding total money.... 

rs10 = 0            # For adding total money.... 
rs20 = 0            # For adding total money.... 

rs50 = 0            # For adding total money.... 

rs100 = 0           # For adding total money.... 

rs200 = 0           # For adding total money.... 

rs500 = 0           # For adding total money.... 

rs2000 = 0          # For adding total money.... 


one = 1                     # element containing money......

two = 2                     # element containing money......

five = 5                    # element containing money......

ten = 10                    # element containing money......

twenty = 20                 # element containing money......

fifty = 50                  # element containing money......

hundred = 100               # element containing money......

t_hun = 200                 # element containing money......

f_hun = 500                 # element containing money......

t_thous = 2000              # element containing money......

while(True):


    if(x <= 0 ):

        print("Please enter valid amount")


    elif(one <= x):

        one += 1

        rs1+= 1


    elif(two <= x):

        two += 2

        rs2+= 1

        
    elif(five <= x):

        five += 5

        rs5+= 1

        
    elif(ten <= x):

        ten += 10

        rs10+= 1


    elif(twenty <= x):

        twenty += 20

        rs20+= 1

        
    elif(fifty <= x):

        fifty += 50

        rs50+= 1

        
    elif(hundred <= x):

        hundred += 100

        rs100+= 1

        
    elif(t_hun <= x):

        t_hun += 200

        rs200+= 1

        
    elif(f_hun <= x):

        f_hun += 500

        rs500+= 1

        
    elif(t_thous <= x):

        t_thous += 2000

        rs2000+= 1


    else:

        break




print(  "Total no. of notes/coins of 1 is       ",  rs1     )

print(  "Total no. of coins of 2 is             ",  rs2     )

print(  "Total no. of notes/coins of 5 is       ",  rs5     )

print(  "Total no. of notes/coins of 10 is      ",  rs10    )

print(  "Total no. of notes/coins of 10 is      ",  rs20    )

print(  "Total no. of notes of 50 is            ",  rs50    )

print(  "Total no. of notes of 100 is           ",  rs100   )

print(  "Total no. of notes of 200 is           ",  rs200   )

print(  "Total no. of notes of 500 is           ",  rs500   )

print(  "Total no. of notes of 2000 is          ",  rs2000  )
