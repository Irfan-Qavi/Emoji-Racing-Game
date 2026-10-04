
# Emoji Racing
# A simple Python terminal game where multiple players compete by earning
# random points in each round.
#
# Project purpose:
# - Demonstrate beginner-friendly Python game logic
# - Practice randomization, loops, input validation, and score tracking
# - Create a fun terminal-based multiplayer game experience
#
# Requirements:
# - Python 3
# - colorama
#
# Run:
#     pip install colorama
#     python main.py
#
# License: MIT
# Copyright (c) 2025


import colorama
import random


# Small helper functions used for formatting and the program flow.
def gap(): print()
def end(): input()


# Return the player(s) tied for the highest score.
def get_winners(players):
    if not players:
        return []

    winners = [players[0]]
    highest_score = players[0].get_score()

    for player in players[1:]:
        score = player.get_score()
        if score > highest_score:
            highest_score = score
            winners = [player]
        elif score == highest_score:
            winners.append(player)

    return winners


# Add a readable ordinal suffix to numbers in input prompts.
def get_rank_suffix(rank):
    if not isinstance(rank, int):
        return ""

    last_two = abs(rank) % 100
    if 10 <= last_two <= 20:
        return "th"

    match abs(rank) % 10:
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
        case _:
            return "th"


class Player:
    """ Store each player's name, symbol, color, and running score. """

    def __init__(self, my_name, my_symbol, my_color):
        self.name = my_name
        self.symbol = my_symbol
        self.color = my_color
        self.score = 0

    def get_name(self):
        return self.name
    
    def get_symbol(self):
        return self.symbol
    
    def get_color(self):
        return self.color
    
    def get_score(self):
        return self.score
    
    def increase_score(self, score):
        self.score += score


# Main game loop: gather settings, create players, and run each round.
if __name__ == "__main__":
    
    colorama.init(autoreset=True)
    colors = [colorama.Back.BLUE, colorama.Back.GREEN, colorama.Back.RED, colorama.Back.WHITE, colorama.Back.YELLOW]
    scale = 1

    players = []
    player_names = []
    player_symbols = []
    player_colors = []

    while True:

        players.clear()
        player_names.clear()
        player_symbols.clear()
        player_colors.clear()

        try:
            gaps = int(input("How many max spaces you want in a window? "))
        except:
            print("Proper input was not given, so starting the game again.")
            continue

        try:
            player_count = int(input("How many players you want? "))
        except:
            print("Proper input was not given, so starting the game again.")
            continue

        gap()
        for i in range(1, player_count + 1):
            name = input(f"Enter {str(i) + get_rank_suffix(i)} player name: ")
            player_names.append(name)

        gap()
        for i in range(1, player_count + 1):
            symbol = input(f"Enter {str(i) + get_rank_suffix(i)} player symbol: ")
            player_symbols.append(symbol)

        gap()
        print("Now you have to choose your color.")
        print("Your options are: ")
        print("0 for Blue")
        print("1 for Green")
        print("2 for Red")
        print("3 for White")
        print("4 for Yellow")
        gap()

        valid_setup = True
        for i in range(1, player_count + 1):
            try:
                color = int(input(f"Enter {str(i) + get_rank_suffix(i)} player color: "))
                if color < 0 or color > 4:
                    raise ValueError("Color must be between 0 and 4.")
            except:
                print("Proper input was not given, so starting the game again.")
                valid_setup = False
                break
            player_colors.append(color)

        if not valid_setup:
            continue

        for i in range(player_count):
            player = Player(player_names[i], player_symbols[i], player_colors[i])
            players.append(player)

        gap()
        try:
            round_count = int(input("How many rounds you want? "))
            gap()
        except:
            print("Proper input was not given, so starting the game again.")
            continue
            
        # Each round has its own minimum and maximum points for random scoring.
        scores = []
        for i in range(1, round_count + 1):
            try:
                minimum_score = int(input(f"How many min points you want in {str(i) + get_rank_suffix(i)} round? "))
                maximum_score = int(input(f"How many max points you want in {str(i) + get_rank_suffix(i)} round? "))
                gap()
            except:
                print("Proper input was not given, so starting the game again.")
                continue
                
            scores.append([minimum_score, maximum_score])
            
        gap()

        # Play each round and display the updated leaderboard.
        for i in range(round_count):
            starter = f"Press Enter to start the {str(i + 1) + get_rank_suffix(i + 1)} round"
            input(starter)
            gap()

            if get_winners(players)[0].get_score() / scale >= gaps:
                scale += 1
            
            print(f"SCALE: 1 Space = {scale} points")
            gap()
            for player in players:
                player.increase_score(random.randint(scores[i][0], scores[i][1]))
                print(f"{player.get_name()}: {player.get_score()} points")
                print(colors[player.get_color()] + " " * int(player.get_score() / scale) + colorama.Back.BLACK + colorama.Fore.WHITE + player.get_symbol())

            gap()
            leaders = get_winners(players)
            if len(leaders) == 1:
                print(f"{leaders[0].get_name()} is leading.")
            elif len(leaders) < len(players):
                print("The following are leading:")
                for leader in leaders:
                    print(leader.get_name())
            else:
                print("Currently, everyone has an equal score.")

            gap()

        # Show the overall winner or tied winners at the end.
        winners = get_winners(players)
        if len(winners) == 1:
            print(f"{winners[0].get_name()} is the winner.")
        elif len(winners) < len(players):
            print("The winners are:")
            for winner in winners:
                print(winner.get_name())
        else:
            print("It's a draw between everyone.")

        match input("Want to play again? "):
            case "Yes":
                print("Ok, game restarted.")
            case "No":
                print("Bye!")
                break
            case _:
                print("Proper input was not given, so starting the game again.")

        gap()

    end()
