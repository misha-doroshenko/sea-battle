class Ship:
    def __init__(self, point: tuple, size: int, orientation: bool) -> None:
        self.point = point
        self.size = size
        self.hp = size
        self.orientation = orientation

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        self._orientation = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, value):
        self._point = value

    @property
    def x(self):
        return self.point[0]

    @property
    def y(self):
        return self.point[1]

    @property
    def id_destroyed(self):
        return True if self.hp == 0 else False
