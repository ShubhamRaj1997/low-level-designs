import datetime
import itertools

from exceptions import TicketExpiredException
from parking_charge_calculator import ParkingChargeCalculator
from singleton import Singleton


class ParkingTicket(object):
    id_iterator = itertools.count()

    def __init__(self, spot):
        self.id = next(self.id_iterator)
        self.spot = spot
        self.__start_time = datetime.datetime.now()
        self.__end_time = None
        self.__cost = None

    @property
    def start_time(self):
        return self.__start_time

    @property
    def cost(self):
        if not self.__cost:
            time_hr = (self.end_time - self.start_time).total_seconds() / 3600
            self.__cost = ParkingChargeCalculator().calculate(time_hr)
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def end_time(self):
        if not self.__end_time:
            self.__end_time = datetime.datetime.now()
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time):
        if self.__end_time:
            raise TicketExpiredException(f"ticket with {self.id} is expired already!")
        self.__end_time = end_time


class ParkingTicketHelper(metaclass=Singleton):
    def __init__(self):
        self.tickets = {}

    def generate_ticket(self, spot):
        ticket = ParkingTicket(spot)
        self.tickets[ticket.id] = ticket
        return ticket.id

    def get_ticket(self, ticket_id):
        return self.tickets.get(ticket_id)

    def release_ticket(self, ticket_id):
        print("tickets are ", self.tickets)
        ticket = self.tickets.pop(ticket_id)
        ticket.end_time = datetime.datetime.now()
        return ticket
