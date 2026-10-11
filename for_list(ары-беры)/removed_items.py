from random import randint

n = int(input('n: '))
l = [randint(1, 10) for i in range(n)]

print(l)

seen = [False] * 11
new_l = []
for number in l:
    if seen[number] == False:
        new_l.append(number)
        seen[number] = True

print(new_l)
