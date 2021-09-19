from abc import ABC, abstractmethod

from exceptions import MethodNotImplementedException
from parking_floor import ParkingFloor


class ParkingFloorInfo(object):
    def __init__(self, floor_id, park_type_slots_data, floor_displays):
        self.floor_displays = floor_displays
        self.park_type_slots_data = park_type_slots_data
        self.floor_id = floor_id


class ParkingFloorCreator(ABC):

    @abstractmethod
    def factory_method(self, parking_floor_info):
        raise MethodNotImplementedException("factory_method not implemented!")

    def set_floor_spots_info(self, parking_floor_info):
        assert isinstance(parking_floor_info, ParkingFloorInfo)
        # do some validation here if needed
        return self.factory_method(parking_floor_info)


class ParkingFloorCreatorV1(ParkingFloorCreator):

    def factory_method(self, parking_floor_info):
        return ParkingFloor(parking_floor_info.floor_id, parking_floor_info.park_type_slots_data,
                            parking_floor_info.floor_displays)

# similarly we can have a ParkingFloorCreatorV2 which can return other type of ParkingFloor object, say ParkingFloorV2 and do some manipulation over parking_floor_info


