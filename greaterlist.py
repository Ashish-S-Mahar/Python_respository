#  In this file we observe which is greater list 

list = [1,4,2,6,8,10]

list.append(13)
list.append(11)

def func(list):
    lar = list[0]
    for li in list:
        if(li>lar):
            lar = li
    print(lar)
func(list)


# adding two list without using append


list = [12,34,23,56]
print(list)
li = [0]
x = int(input("Enter the value... "))
li[0] = x 
y = li + list
print(y)
