count = 0
while True:
    num = int(input("Enter your number: "))
    if num < 0:
        break
    count += num
print(count)