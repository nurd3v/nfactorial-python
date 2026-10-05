x = int(input("Enter your sum: "))
percentage = 12
year = int(input("How many years you want?: "))
circle = 0
result = 0
bill = 0
summary = 0
summary2 = 0
while circle <= year:
    bill = x * percentage / 100 # 12.000 tenge
    result = bill + x    # x + 12.000tenge 
    summary = result * year
    circle += 1
    summary2 = bill * year
print("Деньги которые лежат у тебя на счету: ", summary, "Твоя чистая прибыль с процентами: ", summary2 )