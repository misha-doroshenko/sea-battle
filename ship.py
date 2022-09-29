class GeneralShipDescriptor:
    def __set_name__(self, owner, name):
        self.protected_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.protected_name)

    def __set__(self, instance, value):
        setattr(instance, self.protected_name, value)


class Ship:
    point = GeneralShipDescriptor()
    size = GeneralShipDescriptor()
    hp = GeneralShipDescriptor()
    orientation = GeneralShipDescriptor()

    def __init__(self, point: tuple, size: int, orientation: bool) -> None:
        self.point = point
        self.size = size
        self.hp = size
        self.orientation = orientation

    @property
    def x(self):
        return self.point[0]

    @property
    def y(self):
        return self.point[1]

    @property
    def id_destroyed(self):
        return True if self.hp == 0 else False
