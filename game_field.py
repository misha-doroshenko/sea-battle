import random
from ship import Ship


class GameField:
    FIELD_SIZE = 10

    def __init__(self) -> None:
        self._field: list[list[str | Ship]] = [["[ ]" for _ in range(GameField.FIELD_SIZE + 2)] for _ in range(GameField.FIELD_SIZE + 2)]

    def print_field(self) -> None:
        print("    A  B  C  D  E  F  G  H  I  J")
        for i in range(1, GameField.FIELD_SIZE + 1):
            if i < GameField.FIELD_SIZE:
                print(i, end="  ")
            else:
                print(i, end=" ")
            for j in range(1, GameField.FIELD_SIZE + 1):
                if isinstance(self._field[i][j], Ship):
                    print(" ▢ ", end="")
                else:
                    print("[ ]", end="")
            print()

    def set_ship_on_field(self, ship: Ship) -> None:
        if ship.orientation:
            self._field[ship.y][ship.x - 1] = "[•]"
            self._field[ship.y][ship.x + ship.size] = "[•]"

            for i in range(ship.x - 1, ship.x + ship.size + 1):
                self._field[ship.y - 1][i] = "[•]"
                self._field[ship.y + 1][i] = "[•]"

            for i in range(ship.x, ship.x + ship.size):
                self._field[ship.y][i] = ship

        else:
            self._field[ship.y - 1][ship.x] = "[•]"
            self._field[ship.y + ship.size][ship.x] = "[•]"

            for i in range(ship.y - 1, ship.y + ship.size + 1):
                self._field[i][ship.x - 1] = "[•]"
                self._field[i][ship.x + 1] = "[•]"

            for i in range(ship.y, ship.y + ship.size):
                self._field[i][ship.x] = ship

    def get_random_ship_args(self, ship_size: int) -> tuple:
        """
        orientation: True - horizontal
                     False - vertical
        """
        orientation = random.choice([True, False])
        if orientation:
            while True:
                start_position_x = random.randint(1, GameField.FIELD_SIZE - ship_size + 1)
                start_position_y = random.randint(1, GameField.FIELD_SIZE)
                fit_check = self.check_fit_horizontal(start_position_x, start_position_y, ship_size)
                if fit_check is True:
                    break
        else:
            while True:
                start_position_x = random.randint(1, GameField.FIELD_SIZE)
                start_position_y = random.randint(1, GameField.FIELD_SIZE - ship_size + 1)
                fit_check = self.check_fit_vertical(start_position_x, start_position_y, ship_size)
                if fit_check is True:
                    break

        return (start_position_x, start_position_y), ship_size, orientation

    def check_fit_horizontal(self, x: int, y: int, ship_size: int) -> bool:
        checks = []

        for i in range(x, x + ship_size):
            if self._field[y][i] == "[ ]":
                checks.append(True)
            else:
                checks.append(False)

        return all(checks)

    def check_fit_vertical(self, x: int, y: int, ship_size: int) -> bool:
        checks = []

        for i in range(y, y + ship_size):
            if self._field[i][x] == "[ ]":
                checks.append(True)
            else:
                checks.append(False)

        return all(checks)

    def fill_field_rand(self):
        self.set_ship_on_field(Ship(*self.get_random_ship_args(4)))         # setting one 4-decked ship

        for _ in range(2):
            self.set_ship_on_field(Ship(*self.get_random_ship_args(3)))     # setting two 3-decked ships

        for _ in range(3):
            self.set_ship_on_field(Ship(*self.get_random_ship_args(2)))     # setting 3 2-decked ships

        for _ in range(4):
            self.set_ship_on_field(Ship(*self.get_random_ship_args(1)))     # setting 4 single-decked ships


gf = GameField()
gf.fill_field_rand()
# gf.print_field_check()
gf.print_field()