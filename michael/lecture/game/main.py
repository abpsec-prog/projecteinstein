

import random
#Create a Rock, Paper, Scissors Game
def main():
    state = ['rock','paper','scissors']
    user_input =("Enter a valid input from the list: ")
    human = take_userinput(user_input,state)
    computer = make_computer_choice(state)
    #result = take_userinput(user_input,state)
    print(computer)

def take_userinput(user_input,state):
    #pass
    #rock, paper, or scissors

    while user_input not in state:
        user_input = input("Choose one of the items(rock, paper, scissors) : ")
    return user_input

def make_computer_choice(state):
    computer_choice = random.choice(state)
    return computer_choice

# Function check_result()
def check_result(human, computer):
    if human == computer:
        return "It's a draw"

    elif (human == "rock" and computer == "scissors"):
        return "Rock wins"

    elif (human == "scissors" and computer == "paper"):
        return "Scissors wins"

    elif (human == "paper" and computer == "rock"):
        return "Paper wins"

main()