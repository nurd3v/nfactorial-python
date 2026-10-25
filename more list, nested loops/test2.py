from random import randint
n = int(input("Enter your number: "))

count = [0] * 10
for i in range(n):
    number = randint(0, 9)
    print(number, end= " ")
    count[number] += 1
print()


#number, count[number]
answer = 0
for number in range(10):
    if count [number] > count [answer]:
        answer = number
print("The most frequent number: ", answer)