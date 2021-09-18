import itertools


class ParkingSpot(object):
    id_iterator = itertools.count()

    def __init__(self, spot_type, floor, _id=None, occupied=None):
        self._id = _id or next(self.id_iterator)
        self.spot_type = spot_type
        self.occupied = occupied
        self.floor = floor
