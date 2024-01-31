from Baseball_Team_Manager_Classes_Steven import Player
from datetime import datetime

positions = ("C", "1B", "2B", "3B", "SS",
                 "LF", "CF", "RF", "P")


def separator():
    print("=*50")


def title():
    print("\t\t\t\t Baseball Team Manager")


def date():
    current_date = datetime.now().date()
    print("CURRENT DATE:\t", current_date)
    game_date = datetime.fromisoformat(input("GAME DATE:\t\t ")).date()
    days = (game_date - current_date).days
    print("DAYS UNTIL GAME:", days)


def menu_options():
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")


def add_player():
    first_name = input("First name: ").title()
    last_name = input("Last name: ").title()
    position = get_player_position()
    at_bats = get_at_bats()
    hits = get_hits(at_bats)

    player = Player(first_name, last_name, position, at_bats, hits)
    players.append(player)
    print(f"Player {player.full_name} was added. \n")


def get_player_position():
    while True:
        position = input("Position: ").upper()
        if position in positions:
            return position
        else:
            print("Invalid position. Please enter correctly.")
            print("Valid positions are:", positions)


def get_at_bats():
    while True:
        try:
            at_bats = int(input("At bats: "))
        except ValueError:
            print("Invalid integer. Please try again")
            continue
    if at_bats < 0 or at_bats > 500:
        print("Invalid entry. Must be between 0 and 500")
    else:
        return at_bats


def get_hits(at_bats):
    while True:
        try:
            hits = int(input("Hits: "))
        except ValueError:
            print("Invalid integer. Please try again")
            continue
    if hits < 0 or hits > at_bats:
        print(f"Invalid entry. Must be between 0 and {at_bats}")
    else:
        return hits


def display_lineup(players):
    if players == None:
        print("No players in the lineup")
    else:
        print(f'{"":3}{"Player":40}{"POS":6}{"AB":>6}{"H":>6}{"AVG":>8}')
        separator()
        for i, player in enumerate(players):
            print(f'{i:<3d}{player.full_name:40}{player.position:6}{player.atBats:6d}{player.hits:6d}{player.batting_avg:8.3f}')
        print()


def display_positions():
    print("POSITIONS")
    print(','.join(positions))


def main():
    separator()
    title()
    menu_options()
    display_positions()
    separator()

    players = []

    while True:
        try:
            choice = int(input("Menu option: "))
        except ValueError:
            choice = -1

        if choice == 1:
            display_positions(players)
        elif choice == 2:
            add_player(players)
        elif choice == 7:
            print("Bye!")
            break
