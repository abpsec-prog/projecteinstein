

# While loop to check even numbers
def check_input():
    num = int(input("Please type a number: "))
    
    while num % 2 == 0:
        print(f"{num} is an even number.TRy again")
        num = int(input("Please type another number: "))
    
    print(f"{num} is an odd number.The code stops")

check_input()