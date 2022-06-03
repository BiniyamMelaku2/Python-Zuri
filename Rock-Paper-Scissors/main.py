import random

possible_actions = ["R", "P", "S"]
random_action = random.choice(possible_actions)
player_action = input("\nEnter a choice \n('R' for 'rock',\n 'P' for 'paper',\n 'S' for 'scissors'):\n")

while player_action not in possible_actions:
    print("{}: is invalid! Pick an option between 'R', 'P' or 'S'".format(player_action))
    player_action = input("\nEnter a choice \n('R' for 'rock',\n 'P' for 'paper',\n 'S' for 'scissors'):\n")

while player_action == random_action:
    if player_action == "R":
        print(f"\nPlayer (Rock): CPU (Rock)\n")
    elif player_action == "P":
        print(f"\nPlayer (Paper): CPU (Paper)\n")
    elif player_action == "S":
        print(f"\nPlayer (Scissors): CPU (Scissors)\n")
    
    print(f"\nBoth players selected {player_action}. It's a tie! restarting the game:\n")
    player_action = input("Enter a choice \n('R' for 'rock',\n 'P' for 'paper',\n 'S' for 'scissors'):\n")
    random_action = random.choice(possible_actions)
    while player_action not in possible_actions:
        print("{}: is Invalid! Pick an option between 'R', 'P' or 'S'".format(player_action))
        player_action = input("\nEnter a choice \n('R' for 'rock',\n 'P' for 'paper',\n 'S' for 'scissors'):\n")
    
if player_action == "R":
    if random_action == "S":
        print(f"\nPlayer (Rock): CPU (Scissors)\n")
        print("Rock smashes scissors! You win!\n")
    else:
        print(f"\nPlayer (Rock): CPU (Paper)\n")
        print("Paper covers rock! You lose.\n")
elif player_action == "P":
    if random_action == "R":
        print(f"\nPlayer (Paper): CPU (Rock)\n")
        print("Paper covers rock! You win!\n")
    else:
        print(f"\nPlayer (Paper): CPU (Scissors)\n")
        print("Scissors cuts paper! You lose.\n")
elif player_action == "S":
    if random_action == "P":
        print(f"\nPlayer (Scissors): CPU (Paper)\n")
        print("Scissors cuts paper! You win!\n")
    else:
        print(f"\nPlayer (Scissors): CPU (Rock)\n")
        print("Rock smashes scissors! You lose.\n")