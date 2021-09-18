from enums import ParkingSpotType
from models.floor_parking_spot import FloorHandicappedParkingSpots, FloorLargeParkingSpots, FloorMotorBikeParkingSpots, \
    FloorCompactParkingSpots


class FloorConstants(object):
    DEFAULT_CAPACITY = 20


ParkingSpotTypeFloorSpotsMap = {
    ParkingSpotType.HANDICAPPED: FloorHandicappedParkingSpots,
    ParkingSpotType.LARGE: FloorLargeParkingSpots,
    ParkingSpotType.MOTORBIKE: FloorMotorBikeParkingSpots,
    ParkingSpotType.COMPACT: FloorCompactParkingSpots,

}
