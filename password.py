chance = 0
attempt = 3
while chance < 3:
    password = input("Enter your password: ")
    while True:
        if password == "Nfac129!_":
            print("Correct password!")
            break
        elif password != "Nfac129!_":
            attempt -= 1
            print(f"You have {attempt} chance")
            if attempt == 0:
                print("Sorry you spilled your chance")
            break   
       
    chance += 1