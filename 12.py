i = 0
while True:
    num = int(input("Enter your number: "))
    while i < num:
        i += 1
        print(i)
        if i % 2 == 0:
            continue