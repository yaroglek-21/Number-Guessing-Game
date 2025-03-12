import random

def game_logic():
    print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.\n You have few chances to guess the correct number.")
    print("<----------------------------------------------------------->")
    print("<----------------------------------------------------------->")
    print("Please select the difficulty level:\n 1. Easy (10 chances)\n 2. Medium (5 chances)\n 3. Hard (3 chances)")
    print("<----------------------------------------------------------->")
    select_level = int(input("Enter your choise: "))

    attempts = 0
    max_attempts = 0
    if select_level == 1:
        max_attempts = max_attempts + 10
    elif select_level == 2:
        max_attempts = max_attempts + 5
    elif select_level == 3:
        max_attempts = max_attempts + 3
    else:
        print("You enter incorrect choice")
        
    print(f"You have {max_attempts} attempts!\n Let's start the game!")
    pc_num = random.randint(1, 100)
    while attempts < max_attempts:
        attempts = attempts + 1
        inp_num = int(input("Enter you guess: "))
        if inp_num < 0 or inp_num > 100:
            print("You enter incorrect number")
        elif inp_num < pc_num:
            print(f"Incorrect! The number is greater than {inp_num}.")
        elif inp_num > pc_num:
            print(f"Incorrect! The number is less than {inp_num}.")
        elif inp_num == pc_num:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
    else:
        print("Sorry, you loss")
        
        
game_logic()
while True:
    cont = input("Do you want to play again? (Y/N)")
    if "y" in cont or "Y" in cont:
        game_logic()
    elif "n" in cont or "N" in cont:
        print("Thanks for game!")
        break
    else:
        print("Select an option")





