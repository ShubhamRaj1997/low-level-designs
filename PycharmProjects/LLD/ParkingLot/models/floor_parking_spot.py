import datetime

from enums import ParkingSpotType
from exceptions import NoFreeSpotFoundException, SpotAlreadyOccupiedException


class FloorParkingSpots(object):
    def __init__(self, spot_type, spots):
        self.spot_type = spot_type
        self.spots = spots
        self.__is_occupied = None

    @property
    def is_occupied(self):
        return all([spot.occupied for spot in self.spots])

    @is_occupied.setter
    def is_occupied(self, is_occupied):
        self.__is_occupied = is_occupied

    def __find_spot_by_id(self, spot_id):
        for parking_spot in self.spots:
            if parking_spot._id == spot_id:
                return parking_spot
        raise f"spot with id: {spot_id} not found!"

    def add_spot(self, spot):
        self.spots.add(spot)

    def available_spots(self):
        available_spots = []
        for spot in self.spots:
            if not spot.occupied:
                available_spots.append(spot)
        return available_spots

    # occupy_spot and free_spot can be merged together!

    def occupy_spot(self, spot_id):
        spot = self.__find_spot_by_id(spot_id)
        if spot.occupied:
            raise SpotAlreadyOccupiedException(f"Spot {spot_id} is already occupied on floor: {spot.foor}")
        spot.occupied = datetime.datetime.now()

    def free_spot(self, spot_id):
        spot = self.__find_spot_by_id(spot_id)
        occupied_time = (datetime.datetime.now()-spot.occupied).total_seconds()
        spot.occupied = None
        return occupied_time

    def remove_spot(self, spot_id):
        spot = self.__find_spot_by_id(spot_id)
        self.spots.remove_spot(spot)

    def find_free_spot(self):
        print("available spots are:\n")
        for spot in self.spots:
            print("spot values are ", spot._id, spot.occupied, spot.spot_type)
            if not spot.occupied:
                print("returning spot")
                return spot
        raise NoFreeSpotFoundException(f"No spot found for type {self.spot_type}")

    def capacity(self):
        return len(self.spots)


class FloorHandicappedParkingSpots(FloorParkingSpots):
    def __init__(self, spots):
        super(FloorHandicappedParkingSpots, self).__init__(ParkingSpotType.HANDICAPPED, spots)


class FloorLargeParkingSpots(FloorParkingSpots):
    def __init__(self, spots):
        super(FloorLargeParkingSpots, self).__init__(ParkingSpotType.LARGE, spots)


class FloorCompactParkingSpots(FloorParkingSpots):
    def __init__(self, spots):
        super(FloorCompactParkingSpots, self).__init__(ParkingSpotType.COMPACT, spots)


class FloorMotorBikeParkingSpots(FloorParkingSpots):
    def __init__(self, spots):
        super(FloorMotorBikeParkingSpots, self).__init__(ParkingSpotType.MOTORBIKE, spots)
