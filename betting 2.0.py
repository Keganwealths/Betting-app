import random

while True:
    # Get the odds from the user
    home_odds = float(input("Enter home odds: "))
    draw_odds = float(input("Enter draw odds: "))
    away_odds = float(input("Enter away odds: "))
    
    # Choose a winner at random
    winner_odds = random.choice([home_odds, draw_odds, away_odds])
    if winner_odds == home_odds:
        winner = "home"
    elif winner_odds == draw_odds:
        winner = "draw"
    else:
        winner = "away"
    
    # Ask the user to pick a winner
    user_pick = input("Which odds do you think will win? (home/draw/away): ")
    
    # Determine the winning odds between the user pick and the random winner
    if user_pick == "home":
        user_odds = home_odds
    elif user_pick == "draw":
        user_odds = draw_odds
    else:
        user_odds = away_odds
    
    winning_odds = random.choice([user_odds, winner_odds])
    

    # Print the result
    print(f" the winning odds are {winning_odds:.2f}.")
    
    # Ask the user if they want to continue playing
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "no":
        break
