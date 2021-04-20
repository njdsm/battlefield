class Player:
    def __init__(self, name):
        self.name = name
        self.remaining_ships = ["destroyer", "submarine", "battleship 1", "battleship 2", "aircraft carrier"]
        self.my_board = [{"A1": "O", "A2": "O", "A3": "O", "A4": "O", "A5": "O",
                          "A6": "O", "A7": "O", "A8": "O", "A9": "O", "A10": "O"},
                         {"B1": "O", "B2": "O", "B3": "O", "B4": "O", "B5": "O",
                          "B6": "O", "B7": "O", "B8": "O", "B9": "O", "B10": "O"},
                         {"C1": "O", "C2": "O", "C3": "O", "C4": "O", "C5": "O",
                          "C6": "O", "C7": "O", "C8": "O", "C9": "O", "C10": "O"},
                         {"D1": "O", "D2": "O", "D3": "O", "D4": "O", "D5": "O",
                          "D6": "O", "D7": "O", "D8": "O", "D9": "O", "D10": "O"},
                         {"E1": "O", "E2": "O", "E3": "O", "E4": "O", "E5": "O",
                          "E6": "O", "E7": "O", "E8": "O", "E9": "O", "E10": "O"},
                         {"F1": "O", "F2": "O", "F3": "O", "F4": "O", "F5": "O",
                          "F6": "O", "F7": "O", "F8": "O", "F9": "O", "F10": "O"},
                         {"G1": "O", "G2": "O", "G3": "O", "G4": "O", "G5": "O",
                          "G6": "O", "G7": "O", "G8": "O", "G9": "O", "G10": "O"},
                         {"H1": "O", "H2": "O", "H3": "O", "H4": "O", "H5": "O",
                          "H6": "O", "H7": "O", "H8": "O", "H9": "O", "H10": "O"},
                         {"I1": "O", "I2": "O", "I3": "O", "I4": "O", "I5": "O",
                          "I6": "O", "I7": "O", "I8": "O", "I9": "O", "I10": "O"},
                         {"J1": "O", "J2": "O", "J3": "O", "J4": "O", "J5": "O",
                          "J6": "O", "J7": "O", "J8": "O", "J9": "O", "J10": "O"}]
        self.opponent_board = [{"A1": "O", "A2": "O", "A3": "O", "A4": "O", "A5":
                            "O", "A6": "O", "A7": "O", "A8": "O", "A9": "O", "A10": "O"},
                         {"B1": "O", "B2": "O", "B3": "O", "B4": "O", "B5": "O",
                          "B6": "O", "B7": "O", "B8": "O", "B9": "O", "B10": "O"},
                         {"C1": "O", "C2": "O", "C3": "O", "C4": "O", "C5": "O",
                          "C6": "O", "C7": "O", "C8": "O", "C9": "O", "C10": "O"},
                         {"D1": "O", "D2": "O", "D3": "O", "D4": "O", "D5": "O",
                          "D6": "O", "D7": "O", "D8": "O", "D9": "O", "D10": "O"},
                         {"E1": "O", "E2": "O", "E3": "O", "E4": "O", "E5": "O",
                          "E6": "O", "E7": "O", "E8": "O", "E9": "O", "E10": "O"},
                         {"F1": "O", "F2": "O", "F3": "O", "F4": "O", "F5": "O",
                          "F6": "O", "F7": "O", "F8": "O", "F9": "O", "F10": "O"},
                         {"G1": "O", "G2": "O", "G3": "O", "G4": "O", "G5": "O",
                          "G6": "O", "G7": "O", "G8": "O", "G9": "O", "G10": "O"},
                         {"H1": "O", "H2": "O", "H3": "O", "H4": "O", "H5": "O",
                          "H6": "O", "H7": "O", "H8": "O", "H9": "O", "H10": "O"},
                         {"I1": "O", "I2": "O", "I3": "O", "I4": "O", "I5": "O",
                          "I6": "O", "I7": "O", "I8": "O", "I9": "O", "I10": "O"},
                         {"J1": "O", "J2": "O", "J3": "O", "J4": "O", "J5": "O",
                          "J6": "O", "J7": "O", "J8": "O", "J9": "O", "J10": "O"}]

    def display_board(self):
        print(f"{self.name}'s Board")
        i = 0
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("   1 2 3 4 5 6 7 8 9 10")
        while i < len(self.my_board):
            val = str(self.my_board[i].values())
            val = val[14:-3]
            x = ''.join(c for c in val if c not in "',")
            print(rows[i] + "  " + x)
            i += 1
        print("\n")

    def display_remaining_ships(self):
        print(f"{self.name}'s remaining ships: {self.remaining_ships}\n")
