import threading

from constants.floor_constants import ParkingSpotTypeFloorSpotsMap
from enums import ParkingSpotType
from exceptions import SpotAlreadyOccupiedException


class ParkingFloor(object):
    def __init__(self, _id, floor_parking_spots: dict, floor_displays):
        self.__id = _id
        self.__capacity = None
        self.__is_occupied = None
        self.__floor_parking_spots = {
            ParkingSpotType.HANDICAPPED: floor_parking_spots.get(ParkingSpotType.HANDICAPPED,
                                                                 ParkingSpotTypeFloorSpotsMap.get(
                                                                     ParkingSpotType.HANDICAPPED)([])),
            ParkingSpotType.LARGE: floor_parking_spots.get(ParkingSpotType.LARGE,
                                                           ParkingSpotTypeFloorSpotsMap.get(ParkingSpotType.LARGE)([])),
            ParkingSpotType.MOTORBIKE: floor_parking_spots.get(ParkingSpotType.MOTORBIKE,
                                                               ParkingSpotTypeFloorSpotsMap.get(
                                                                   ParkingSpotType.MOTORBIKE)([])),
            ParkingSpotType.COMPACT: floor_parking_spots.get(ParkingSpotType.COMPACT,
                                                             ParkingSpotTypeFloorSpotsMap.get(ParkingSpotType.COMPACT)(
                                                                 [])),
        }
        self.__floor_displays = floor_displays
        self.lock = threading.Lock()

    @property
    def capacity(self):
        # if you have an enumeration that has aliases, too,
        # only the approach using __members__ will print the aliases as well.
        if self.__capacity is None:
            self.__capacity = 0
            for parking_floor_spots in self.__floor_parking_spots.values():
                self.__capacity += parking_floor_spots.capacity
        return self.__capacity

    @property
    def occupied(self):
        if self.__is_occupied is None:
            self.__is_occupied = all(
                parking_floor_spots.is_occupied for parking_floor_spots in self.__floor_parking_spots.values())
        return self.__is_occupied

    def add_spot(self, spot_type, spot):
        self.__floor_parking_spots[spot_type].add_spot(spot)
        self._update_display()

    def remove_spot(self, spot_type, spot_id):
        self.__floor_parking_spots[spot_type].remove_spot(spot_id)
        self._update_display()

    def occupy_spot(self, spot_type, spot_id):
        self.lock.acquire()
        try:
            self.__floor_parking_spots[spot_type].occupy_spot(spot_id)
        except SpotAlreadyOccupiedException as e:
            raise e
        finally:
            self.lock.release()
            self._update_display()

    def free_spot(self, spot_type, spot_id):
        """
        Free the spt
        :param spot_type:
        :param spot_id:
        :return:
        """
        print(f"Free the spot, got the spot type as {spot_type} and spot id is {spot_id}")
        time_occupied = self.__floor_parking_spots[spot_type].free_spot(spot_id)
        self._update_display()
        return time_occupied

    def find_free_spot(self, spot_type):
        return self.__floor_parking_spots[spot_type].find_free_spot()

    def _update_display(self):
        display_data = dict(capacity={}, available={})
        for parking_spot_type in ParkingSpotType:
            display_data["capacity"][parking_spot_type.name] = self.__floor_parking_spots[parking_spot_type].capacity()
            display_data["available"][parking_spot_type.name] = len(
                self.__floor_parking_spots[parking_spot_type].available_spots())
        for floor_display in self.__floor_displays:
            floor_display.display(display_data, self.__id)

