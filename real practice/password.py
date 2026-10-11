chance = 0
attempt = 3
while chance < 3:
    password = input("Enter your password: ")
    if password == "Nfac129!_":
        print("Correct answer!")
        break
    if password != "Nfac129!_":
        attempt -= 1
        print(f"You have {attempt} chance")
        if attempt == 0:
            print("Sorry, you have spilled your full chance")
            break    
    chance += 1