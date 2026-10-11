#Напишиите программу, которая вычисляет сумму скидки в зависимости от суммы продажи. Пусть скидки установлены следующим образом:

#Сумма продажи	Скидка
#0-5000	5%
#5000-15000	12%
#15000-25000	20%
#с выше 25000	30%

sum = int(input("Enter your $: "))

if sum >= 25000:
  total = (sum * 30 / 100)
  print(total)
  print("Total price with sale: ", sum-total)
elif sum >= 15000:
  total = (sum * 20 / 100)
  print(total)
  print("Total price with sale: ", sum-total)
elif sum >= 5000:
  total = (sum * 12 / 100)
  print(total)
  print("Total price with sale: ", sum-total)
elif sum >= 0:
  total = (sum * 5 / 100)
  print(total)
  print("Total price with sale: ", sum-total)
      