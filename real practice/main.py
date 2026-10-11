n = int(input("Enter your number: "))
i = 0
result = 0 
while i<= n:
    totally = 2 ** i
    print(totally)
    i += 1
    result += totally
print("The summary is: ", result)
    
 