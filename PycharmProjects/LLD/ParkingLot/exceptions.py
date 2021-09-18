class FloorAlreadyPresentException(Exception):
    pass


class FloorNotPresentException(Exception):
    pass


class SpotNotFoundException(Exception):
    pass


class NoFreeSpotFoundException(Exception):
    pass


class SpotAlreadyOccupiedException(Exception):
    pass


class TicketExpiredException(Exception):
    pass
