#Take a three-digit number as input and reverse its digits. Leading zeroes are allowed in the
#input. For example, input 123 should output 321.

n = int(input())

a = n // 100
b = (n // 10) % 10
c = n % 10

print(c * 100 + b * 10 + a)