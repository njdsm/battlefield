from player import Player
import time
import shutil

class Game:
    def __init__(self):
        self.name = "Bad-leShip"
        self.player_one = Player("Player One")
        self.player_two = Player("Player Two")
        self.round = 0
        #self.size = shutil.get_terminal_size()

    def run_game(self):
        print("Welcome to Bad-leShip! It's just like the beloved childhood game, just not quite as fun.\n")
        self.player_one.name = input("Player One, what do you want your name to be?\n:")
        print(f"Great! Ok {self.player_one.name}, please pass the screen to Player Two. I'll give you some time...")
        counter = 2
        while counter > 0:
            print(counter)
            time.sleep(1)
            counter -= 1
        print("\n" * 100)
        self.player_two.name = input(f"Player Two, what do you want your name to be?\n"
                                     f"For example your friend chose {self.player_one.name}.\n:")
        self.display_boards()
        print(f"Great, now it's time for {self.player_one.name} to set up his ships. {self.player_two.name} "
              f"please go away.")
        placed_ships = []
        self.player_one.setup_board(placed_ships)
        print("\n" * 20)
        print(f"Great, now it's time for {self.player_two.name} to set up his ships. {self.player_one.name} "
              f"please go away.")
        placed_ships = []
        self.player_two.setup_board(placed_ships)
        print(f"Ok, time to start the game!")
        while len(self.player_one.remaining_ships) > 0 and len(self.player_two.remaining_ships) > 0:
            print("\n" * 20)
            print("Round: " + str(self.round))
            guess = self.player_one.turn_start()
            self.player_two.my_board = self.player_one.hit_check(guess, self.player_two.my_board)
            guess = self.player_two.turn_start()
            self.player_one.my_board = self.player_two.hit_check(guess, self.player_one.my_board)
            self.round += 1

    def display_boards(self):
        self.player_one.display_board()
        self.player_one.display_remaining_ships()
        self.player_two.display_board()
        self.player_two.display_remaining_ships()



