#Write program that takes two integers m and d and prints True if day d of month m 
# is between March 20 (m = 3, d = 20) and June 20 (m = 6, d = 20), and prints False otherwise

day = int(input("Enter day number: "))
month = int(input("Enter month number: "))

if month == 4 or month == 5:
    print("True")
elif month == 3 and day >= 20:
    print("True")
elif month == 6 and day <= 20:
    print("True")
else:
    print("False")    