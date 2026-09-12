#Задача 1: Сумма чисел от 1 до N
# input: 5, output: 15 (1+2+3+4+5)

n = int(input("Enter your number: "))
i = 1
answer = 0
while i <= n:
    answer += i
    i+=1 
print(answer)