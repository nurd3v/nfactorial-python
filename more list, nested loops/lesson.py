n = int(input("Enter your n: "))
m = int(input("Enter your m: "))
list = []
for i in range(1, n):
    list.append(i)
    for number in list:
        if number % 3  == 0:
            list.remove(number)
        elif number % 5 == 0:
            list.remove(number)



print(list)           
print(list[m-1])  
