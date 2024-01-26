from Baseball_Team_Manager_Classes_Steven import Player
from datetime import datetime


def separator():
    print("=*50")


def title():
    print("Baseball Team Manager")


def date():
    current_date = datetime.now().date()
    print("CURRENT DATE:\t", current_date)
    game_date = datetime.fromisoformat(input("GAME DATE:\t\t ")).date()
    days = (game_date - current_date).days
    print("DAYS UNTIL GAME:", days)

date()
