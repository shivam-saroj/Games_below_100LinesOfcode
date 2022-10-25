import random

valid_options = ["Rock", "Paper", "Scissors"]
win_conditions = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}

while True:
    cpu_choice = random.choice(valid_options)
    player_choice = input("Rock, Paper, Scissors, shoot!").capitalize()
    if not player_choice in valid_options:
        print("You must chooce either Rock, Paper, or Scissors.")
    else:
        print(f"You chose {player_choice}, CPU chose {cpu_choice}.")
        if cpu_choice == player_choice:
            print("It's a tie!")
        elif win_conditions[player_choice] == cpu_choice:
            print("You win!")
        else:
            print("You lose.")
        play_again = input("Play again? y/n")
        if not play_again.lower() == "y": break