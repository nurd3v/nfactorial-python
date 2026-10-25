# Пользователь вводит n . Создать список из n случайных чисел от 0 до 9. 
# Вывести новый список, где каждое число заменено на сумму соседних элементов исходного списка (для крайних элементов — один сосед).

from random import randint

n = int(input("Enter your number: "))

numbers = [randint(0, 9) for i in range (n)]
print(numbers)

new_numbers = []

for i in range(len(numbers)):
    if i == 0:
        new_numbers.append(numbers[i + 1])
    elif i == len(numbers) - 1:
        new_numbers.append(numbers[i - 1])
    else:
        new_numbers.append(numbers[i - 1] + numbers[i + 1])
        
print(new_numbers)