from dataclasses import dataclass
from random import choice


@dataclass
class Player:
    name: str = ""
    roshambo: str = ""

    def generate_roshambo(self):
        self.roshambo = "Rock"
        return self.roshambo

    def play(self, Player):
        if Player.roshambo == "Rock" and self.roshambo == "Scissors":
            return Player.roshambo
        if Player.roshambo == "Rock" and self.roshambo == "Paper":
            return self.roshambo
        if Player.roshambo == "Paper" and self.roshambo == "Rock":
            return Player.roshambo
        if Player.roshambo == "Paper" and self.roshambo == "Scissors":
            return self.roshambo
        if Player.roshambo == "Scissors" and self.roshambo == "Paper":
            return Player.roshambo
        if Player.roshambo == "Scissors" and self.roshambo == "Rock":
            return self.roshambo
        if Player.roshambo == self.roshambo:
            return None


@dataclass
class Bart(Player):

    def player_name(self):
        self.name = "Bart"


@dataclass
class Lisa(Player):
    def player_name(self):
        self.name = "Lisa"

    def generate_random_roshambo(self):
        self.roshambo = (choice(["Rock", "Paper", "Scissors"]))
        return self.roshambo


def main():
    print("Roshambo Game")
    name = input("Enter your name: ")
    play_against = input("Would you like to play Bart or Lisa? (b/l): ")
    # if play_against.lower == "b":
