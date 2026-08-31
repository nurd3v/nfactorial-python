n = input()

even = 0
odd = 0

for x in n:
    if int(x) % 2 == 0:
        even += 1
    else:
        odd += 1

print(even, odd)