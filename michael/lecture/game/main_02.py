import random
#Create a Rock, Paper, Scissors Game
def main():
    state = ['rock','paper','scissors']
    user_input =("Enter a valid input from the list: ")
    human = take_userinput(user_input,state)
    computer = make_computer_choice(state)

    c= check_result(human,computer)
    print(f"Computer chose: {computer} and I chose: {human}, Therefore: {c}")
    

    #print(f"Computer chose: {computer} and I chose: {human} Therefore: {print(check_result(human, computer))} ")


def take_userinput(user_input,state):
    while user_input not in state:
        user_input = input("Choose one of the items(rock, paper, scissors) : ")
    return user_input


def make_computer_choice(state):
    computer_choice = random.choice(state)
    return computer_choice


def check_result(human, computer):
    if human == computer:
        return "It's a draw"

    elif (human, computer) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
        return f"{human.capitalize()} wins"

    else:
        return f"{computer.capitalize()} wins"
    


main()