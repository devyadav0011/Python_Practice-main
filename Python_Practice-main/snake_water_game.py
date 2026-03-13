
import random

CHOICES = {
    "s": "Snake",
    "w": "Water",
    "g": "Gun"
}

WIN_MAP = {
    "s": "w",  # s beats w
    "w": "g",  
    "g": "s",  
}


def get_user_choice():
    while True:
        choice = input("Enter your choice — (S)snake, (W)water, (G)gun or (Q)quit: ").strip().lower()
        if choice == 'q':
            return 'q'
        if choice in CHOICES:
            return choice
        print("Invalid input. Type 'S', 'W', 'G' or 'Q'.")


def get_computer_choice():
    return random.choice(list(CHOICES.keys()))


def decide_round(player, computer):
    if player == computer:
        return "draw"
    # player wins if WIN_MAP[player] == computer
    if WIN_MAP[player] == computer:
        return "player"
    return "computer"


def play_round(round_no=None):
    if round_no is not None:
        print(f"\n--- Round {round_no} ---")
    player = get_user_choice()
    if player == 'q':
        return 'quit', None, None
    computer = get_computer_choice()
    print(f"You chose:     {CHOICES[player]}")
    print(f"Computer chose: {CHOICES[computer]}")
    result = decide_round(player, computer)
    if result == "draw":
        print("Result: It's a draw!")
    elif result == "player":
        print("Result: You win this round! 🎉")
    else:
        print("Result: Computer wins this round.")
    return result, player, computer


def play_game():
    print("Welcome to Snake — Water — Gun!")
    print("Rules: Snake > Water, Water > Gun, Gun > Snake")
    print("Play rounds and try to beat the computer. Type 'Q' anytime to quit.\n")

    # Ask number of rounds (best-of) or allow infinite play
    while True:
        mode = input("Choose mode: (1) Best of N rounds  (2) Play until you quit  — enter 1 or 2: ").strip()
        if mode in ('1', '2'):
            break
        print("Enter 1 or 2.")

    if mode == '1':
        while True:
            n = input("Enter odd number of rounds (e.g. 3, 5, 7): ").strip()
            if n.isdigit() and int(n) % 2 == 1 and int(n) > 0:
                total_rounds = int(n)
                break
            print("Please enter a positive odd integer.")
        rounds_to_win = total_rounds // 2 + 1
        player_score = 0
        computer_score = 0
        current_round = 0

        while player_score < rounds_to_win and computer_score < rounds_to_win:
            current_round += 1
            result, p, c = play_round(current_round)
            if result == 'quit':
                print("You quit the game. Thanks for playing!")
                return
            if result == "player":
                player_score += 1
            elif result == "computer":
                computer_score += 1
            print(f"Score => You: {player_score}  Computer: {computer_score}")

        print("\n--- Final Result ---")
        if player_score > computer_score:
            print(f"Congratulations — You won the match {player_score} to {computer_score}! 🏆")
        else:
            print(f"Computer won the match {computer_score} to {player_score}. Better luck next time!")
    else:
        # Infinite mode until user quits
        player_score = 0
        computer_score = 0
        round_no = 0
        while True:
            round_no += 1
            result, p, c = play_round(round_no)
            if result == 'quit':
                print("\nYou quit the game.")
                print(f"Final Score => You: {player_score}  Computer: {computer_score}")
                return
            if result == "player":
                player_score += 1
            elif result == "computer":
                computer_score += 1
            print(f"Score => You: {player_score}  Computer: {computer_score}")


if __name__ == "__main__":
    play_game()

