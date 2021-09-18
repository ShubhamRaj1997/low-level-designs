from ParkingLot.exceptions import FloorAlreadyPresentException, FloorNotPresentException


class ParkingLot(object):
    def __init__(self, address):
        self.__address = address
        self.__floors = []
        self.__entrances = []
        self.__exits = []
        self.__parking_floors = []

    def add_floor(self, floor):
        if floor in self.__floors:
            raise FloorAlreadyPresentException()
        self.__floors.append(floor)

    def remove_floor(self, floor):
        if floor not in self.__floors:
            raise FloorNotPresentException()
        self.__floors.remove(floor)

    def add_entrances(self, entrance):
        self.__entrances.append(entrance)

    def add_exits(self, exit):
        self.__exits.append(exit)

    def add_parking_floors(self, parking_floor):
        self.__parking_floors.append(parking_floor)

    def remove_parking_floors(self, parking_floor):
        self.__parking_floors.remove(parking_floor)


