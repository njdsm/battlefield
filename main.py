from game import Game

if __name__ == '__main__':
    again = True
    while again:
        game = Game()
        winner = game.run_game()
        print(winner)
        user_input = input("\n\n\nWould you like to play again? y/n\n:")
        if user_input != "y":
            again = False
