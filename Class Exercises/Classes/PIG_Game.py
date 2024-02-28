from PIG_Game_Class import Game


def display_welcome():
    print("Let's play PIG!\n")
    print("*See how many turns...")
    print("Game instructions 2")
    print("Game instructions 3")
    print("Game instructions 4\n")


def main():
    display_welcome()
    choice = 'y'
    while choice.lower() == 'y':
        game = Game()
        game.play()

        choice = input("Play again? (y/n): ")
        print("Thanks for playing!")


if __name__ == '__main__':
    main()
