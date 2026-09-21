import sys
n = int(input("Enter n: "))
count = 0
if n < 0:
    print("Illegal input")  
    sys.exit()
while n > 0:
    n = n // 2
    count += 1
print(count)
        
    
    