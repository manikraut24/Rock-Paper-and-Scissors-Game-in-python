#Develop a Python console-based Rock, Paper, Scissors game
import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "player"
    else:
        return "computer"

# Main game loop
def play_game():
    player_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors - Choose your move:")
        player_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'quit' to stop playing): ").lower()

        if player_choice == 'quit':
            break

        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == "player":
            print("You win this round!")
            player_score += 1
        elif result == "computer":
            print("Computer wins this round.")
            computer_score += 1
        else:
            print("It's a draw.")

        print(f"Score - Player: {player_score}, Computer: {computer_score}")

    print("\nFinal Score:")
    print(f"Player: {player_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    play_game()
