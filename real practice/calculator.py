num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

char = str(input("Enter you symbol: "))
plus = "+"
minus = "-"
asd = "*"
das = "/"

if char == plus:
   print(num1 + num2) 
elif char == minus:
    print(num1 - num2)
elif char == asd:
    print(num1 * num2)
elif char == das:
    print(num1 / num2)
