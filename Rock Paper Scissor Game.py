import random
def play_game():
    user_score = 0
    computer_score = 0
    while True:
        print("\n----- Rock-Paper-Scissors Game -----")
        print("Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        user_choice = input("Enter your choice (1-4): ")
        if user_choice == "4":
            print("Exiting the game.")
            break
        elif user_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")
            continue
        user_move = get_user_move(user_choice)
        computer_move = get_computer_move()
        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")
        result = determine_winner(user_move, computer_move)
        if result == "win":
            user_score += 1
            print("You win!")
        elif result == "lose":
            computer_score += 1
            print("You lose!")
        else:
            print("It's a tie!")
        print(f"Your Score: {user_score}")
        print(f"Computer's Score: {computer_score}")
def get_user_move(choice):
    moves = {
        "1": "Rock",
        "2": "Paper",
        "3": "Scissors"
    }
    return moves.get(choice)
def get_computer_move():
    moves = ["Rock", "Paper", "Scissors"]
    return random.choice(moves)
def determine_winner(user_move, computer_move):
    if user_move == computer_move:
        return "tie"
    elif (
        (user_move == "Rock" and computer_move == "Scissors") or
        (user_move == "Paper" and computer_move == "Rock") or
        (user_move == "Scissors" and computer_move == "Paper")
    ):
        return "win"
    else:
        return "lose"
if __name__ == "__main__":
    play_game()
