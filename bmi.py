# Its a body mass index calculater....
x = int(input("Enter your weight in kg:"))
y = float(input("Enter your height in m:"))
z = x//(y*y)
print(z)

if(z<=18):
    print("You is underweight...")
if(z>18 and z<54):
    print("good")
if(z>=54):
    print("You is overweight...")