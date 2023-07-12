import random

def roll_dice():
    """Rolls a six-sided dice and returns the result."""
    return random.randint(1, 6)

def play_game():
    """Plays the dice rolling game."""
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")
    
    player1_score = 0
    player2_score = 0
    
    num_rounds = int(input("Enter the number of rounds: "))
    
    for round_num in range(1, num_rounds + 1):
        print(f"Round {round_num}:")
        
        input(f"{player1_name}, press Enter to roll the dice.")
        player1_roll = roll_dice()
        print(f"{player1_name} rolled a {player1_roll}.\n")
        
        input(f"{player2_name}, press Enter to roll the dice.")
        player2_roll = roll_dice()
        print(f"{player2_name} rolled a {player2_roll}.\n")
        
        if player1_roll > player2_roll:
            print(f"{player1_name} wins the round!\n")
            player1_score += 1
        elif player2_roll > player1_roll:
            print(f"{player2_name} wins the round!\n")
            player2_score += 1
        else:
            print("It's a tie!\n")
    
    print("Game Over!\n")
    print(f"Final Scores:\n{player1_name}: {player1_score}\n{player2_name}: {player2_score}")
    
    if player1_score > player2_score:
        print(f"{player1_name} wins the game!")
    elif player2_score > player1_score:
        print(f"{player2_name} wins the game!")
    else:
        print("It's a tie!")

# Run the game
play_game()
