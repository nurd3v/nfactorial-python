# Выведи числа от 1 до 10, но пропускай все чётные числа. Используй continue.
i = 0
while i < 10:
    i+=1
    if i % 2 == 0:
        continue
    print(i)