
while True:
    print("Welcome to Cyberpunk Escape Room!")

    hacker_name = input("Enter your hacker name: ")

    print(f"Hello {hacker_name}!")
    print("You are trapped inside a building.")
    print("You need to escape!")

    print("1. Red Door")
    print("2. Blue Door")

    user_choice = input("Choose a door (1 or 2): ")

    if user_choice == "1":
        print("Security drones caught you!")
        print(f"Game Over, {hacker_name}!")
        continue_game = input("Do you want to try again? (yes/no): ")
        if continue_game == "yes":
            continue
        else:
            print("Thanks for playing!")
            break

    elif user_choice == "2":
        print("You found a locked door!")

        passcode = int(input("Enter the passcode (Hint: 1-0): "))

        if passcode == 1234:
            print("Door unlocked!")
            print(f"Congratulations {hacker_name}! You escaped!")

        else:
            print("Wrong passcode!")
            print(f"Game Over, {hacker_name}!")
        break

    else:
        print("Invalid choice!")
        print("Game Over!")
        break
