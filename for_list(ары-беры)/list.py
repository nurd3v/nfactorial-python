n = int(input("Enter your number: "))
list = []
for i in range(n):
    numbers = int(input("Enter your n numbers: "))
    list.append(numbers)
print(list)


x = int(input("Enter your x: "))
for number in list:
    if number == x:
        print(x, end= " ")

for number in list:
    if number != x:
        print(number, end= " ")
        
print()
