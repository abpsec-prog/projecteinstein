def game_rps():
    state = ["rock", "paper", "scissors"]
    ans = input("Please enter either Rock, Paper, or Scissors: ").lower().strip()

    # Continue prompting until a valid input is entered
    while ans not in state:
        print("Invalid input. Please try again.")
        ans = input("Please enter either Rock, Paper, or Scissors: ").lower().strip()

    print(f"You typed '{ans}'. This ends the loop.")

    game_rps()
    