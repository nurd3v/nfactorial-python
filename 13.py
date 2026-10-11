from random import randint

n = int(input("Enter your number: "))
numbers = []
for i in range(n):
    random = (randint(1, 100))
    print (random)
    numbers.append(random)
print("Your minimum count is: ", min(numbers))