from dataclasses import dataclass
import random


@dataclass
class Card:
    rank: str
    suit: str

    def playing_card(self):
        return f"{self.rank} of {self.suit}"


@dataclass
class Deck:
    def __init__(self):
        self.cards = []
        self.deck_of_cards()

    def deck_of_cards(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


def main():
    print("Card Dealer")
    deck = Deck()
    deck.shuffle()
    print(f"\nI have shuffled {len(deck.cards)} cards.")
    number_of_cards_dealt = int(input("\nHow many cards would you like?: "))
    print("\nHere are your cards:")
    for i in range(number_of_cards_dealt):
        card = deck.deal_card()
        if card:
            print(card.playing_card())
        else:
            print("Out of Cards")
    print(f"\nThere are {len(deck.cards)} cards left in the deck.")
    print("\nGood luck!")


if __name__ == "__main__":
    main()
