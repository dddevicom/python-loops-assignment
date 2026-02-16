# Player Score Calculator with Error Handling
player_name = input("Enter player name: ")
try:
    games_played = int(input("Enter number of games played: "))
    total_score = int(input("Enter total score: "))

    if games_played <= 0:
        print("Games played must be greater than 0.")
    else:
        average_score = total_score / games_played
        print("\n--- Player Score Summary ---")
        print(f"Player: {player_name}")
        print(f"Games Played: {games_played}")
        print(f"Total Score: {total_score}")
        print(f"Average Score: {average_score:.2f}")
except ValueError:
    print("Please enter valid numeric values.")
