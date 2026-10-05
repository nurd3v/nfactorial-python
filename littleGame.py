from random import randint

target = randint(1, 100)
tryNumbers = 0
# print("secret", target)


while True:
    n = int(input("Enter your guess: "))
    tryNumbers += 1

    if n < target:
        print("Больше")
    elif n > target:
        print("Меньше")
    else:
        print(f"All right, попал прямо в точку! Попыток: {tryNumbers}")
        break