def get_valid_name():
    """
   Prompts the user to enter a name.
    The fn continues to ask for input using a while loop
    until the name has at least 7 characters.
    """
    name = input("Enter your name (at least 7 characters): ").strip()
    # the strip() removes whitespace
    
    # Continue prompting while the name length is less than 7
    #len() method
    while len(name) < 7:
        print("Invalid input. The name must be at least 7 characters long.")
        name = input("Please enter your name again: ").strip()
    
    print(f"Accepted! Your name is: {name}")
    return name

print(get_valid_name())