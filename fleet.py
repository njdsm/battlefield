from ship import Ship


class Fleet:
    def __init__(self):
        self.ships = []
        #self.remaining_ships = (["destroyer", 2], ["submarine", 3], ["battleship 1", 4], ["battleship 2", 4], ["aircraft carrier", 5])
        self.remaining_ships = (["destroyer", 2], ["submarine", 3])
        for i in self.remaining_ships:
            self.ships.append(Ship(i[0], i[1]))