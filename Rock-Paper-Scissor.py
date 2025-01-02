import random

# Function to get the computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display the score
def display_score(user_score, computer_score, rounds):
    print(f"\nScore after {rounds} rounds:")
    print(f"  You: {user_score}")
    print(f"  Computer: {computer_score}")

# Function to get the number of rounds
def get_rounds():
    while True:
        try:
            rounds = int(input("Enter the number of rounds (best of): "))
            if rounds > 0 and rounds % 2 != 0:
                return rounds
            else:
                print("Please enter a positive odd number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main game loop
def play_game():
    print("\nWelcome to Rock-Paper-Scissors!")
    rounds = get_rounds()
    target_score = (rounds // 2) + 1  # Number of wins needed to secure the match

    user_score = 0
    computer_score = 0
    current_round = 1

    while user_score < target_score and computer_score < target_score:
        print(f"\nRound {current_round}: Choose rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer's choice: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("This round is a tie!")

        display_score(user_score, computer_score, current_round)
        current_round += 1

    # Final result
    if user_score > computer_score:
        print("\nCongratulations! You won the match!")
    else:
        print("\nComputer wins the match. Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_game()
