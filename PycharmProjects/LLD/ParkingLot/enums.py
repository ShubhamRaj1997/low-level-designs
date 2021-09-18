from enum import Enum


class VehicleType(Enum):
    CAR = 1
    BUS = 2
    TRUCK = 3
    BIKE = 4


class ParkingSpotType(Enum):
    COMPACT = 1
    HANDICAPPED = 2
    LARGE = 3
    MOTORBIKE = 4


class ParkingTicketStatus(Enum):
    ACTIVE = 1
    PAID = 2
    LOST = 3


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Customer:
    def __init__(self, name, address, email, phone):
        self.__address = address
        self.__name = name
        self.__email = email
        self.__phone = phone
