from ship import Ship


class Fleet:
    def __init__(self):
        self.ship = []
        self.remaining_ships = (["destroyer", 2], ["submarine", 3], ["battleship 1", 4], ["battleship 2", 4], ["aircraft carrier", 5])
        for i in self.remaining_ships:
            self.ship.append(Ship(i[0], i[1]))