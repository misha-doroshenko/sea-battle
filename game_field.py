import random


class GameField:
    FIELD_SIZE = 10

    def __init__(self) -> None:
        self._field = [["[ ]" for _ in range(GameField.FIELD_SIZE + 2)] for _ in range(GameField.FIELD_SIZE + 2)]
        self._field_check = [["[ ]" for _ in range(GameField.FIELD_SIZE + 2)] for _ in range(GameField.FIELD_SIZE + 2)]

    def print_field(self) -> None:
        print("    A  B  C  D  E  F  G  H  I  J")
        for i in range(1, GameField.FIELD_SIZE + 1):
            if i < GameField.FIELD_SIZE:
                print(i, end="  ")
            else:
                print(i, end=" ")
            for j in range(1, GameField.FIELD_SIZE + 1):
                print(self._field[i][j], end="")
            print()

    def print_field_check(self) -> None:
        for i in range(0, GameField.FIELD_SIZE + 2):
            for j in range(0, GameField.FIELD_SIZE + 2):
                print(self._field_check[i][j], end="")
            print()

    def create_ship(self, ship_size: int, orientation: bool) -> None:
        """
        orientation: True - horizontal
                     False - vertical
        """
        if orientation:
            while True:
                start_position_x = random.randint(1, GameField.FIELD_SIZE - ship_size + 1)
                start_position_y = random.randint(1, GameField.FIELD_SIZE)
                fit_check = self.check_fit_horizontal(start_position_x, start_position_y, ship_size)
                if fit_check is True:
                    break

            self._field_check[start_position_y][start_position_x - 1] = "[*]"
            self._field_check[start_position_y][start_position_x + ship_size] = "[*]"

            for i in range(start_position_x - 1, start_position_x + ship_size + 1):
                self._field_check[start_position_y - 1][i] = "[*]"
                self._field_check[start_position_y + 1][i] = "[*]"

            for i in range(start_position_x, start_position_x + ship_size):
                self._field_check[start_position_y][i] = " # "
                self._field[start_position_y][i] = " # "

        else:
            while True:
                start_position_x = random.randint(1, GameField.FIELD_SIZE)
                start_position_y = random.randint(1, GameField.FIELD_SIZE - ship_size + 1)
                fit_check = self.check_fit_vertical(start_position_x, start_position_y, ship_size)
                if fit_check is True:
                    break

            self._field_check[start_position_y - 1][start_position_x] = "[*]"
            self._field_check[start_position_y + ship_size][start_position_x] = "[*]"

            for i in range(start_position_y - 1, start_position_y + ship_size + 1):
                self._field_check[i][start_position_x - 1] = "[*]"
                self._field_check[i][start_position_x + 1] = "[*]"

            for i in range(start_position_y, start_position_y + ship_size):
                self._field_check[i][start_position_x] = " # "
                self._field[i][start_position_x] = " # "

    def check_fit_horizontal(self, x: int, y: int, ship_size: int) -> bool:
        checks = []

        for i in range(x, x + ship_size):
            if self._field_check[y][i] == "[ ]":
                checks.append(True)
            else:
                checks.append(False)

        return all(checks)

    def check_fit_vertical(self, x: int, y: int, ship_size: int) -> bool:
        checks = []

        for i in range(y, y + ship_size):
            if self._field_check[i][x] == "[ ]":
                checks.append(True)
            else:
                checks.append(False)

        return all(checks)

    def fill_field_rand(self):

        self.create_ship(4, False)

        self.create_ship(3, True)
        self.create_ship(3, False)

        self.create_ship(2, True)
        self.create_ship(2, True)
        self.create_ship(2, True)

        self.create_ship(1, True)
        self.create_ship(1, True)
        self.create_ship(1, True)
        self.create_ship(1, True)

gf = GameField()
gf.fill_field_rand()
# gf.print_field_check()
gf.print_field()