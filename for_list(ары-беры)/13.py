from random import randint

n = int(input("Enter your n: "))
numbers = []
for i in range(n):
    numbers.append(randint (1, 100))
print(numbers)
min_number = numbers[0]

for number in numbers:
    if min_number > number:
        min_number = number
print(min_number)