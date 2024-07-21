#  Reversing a list without using reverse


x = ["hii", "hello", "hey","why",2," ",]
# x = len(x)
print(x)
y = []
count = 0
for i in range(len(x)-1,-1,-1):

    y.append(x[i])
    
print(y)



