from constants.floor_constants import ParkingSpotTypeFloorSpotsMap
from enums import ParkingSpotType
from exceptions import NoFreeSpotFoundException
from models.floor_display import FloorDisplay
from models.parking_spot import ParkingSpot
from models.ticket import ParkingTicketHelper
from parking_floor import ParkingFloor


def take_input_int(msg):
    return int(input(msg))


def take_input_str(msg):
    return input(msg)


def enter_spot_type():
    return int(input(
        "Select Parking Spot Type:\nEnter 2 for Handicapped parking type\nEnter 3 for Large parking type\nEnter 1 for Compact parking type\nEnter 4 for MotorCycle parking type\n"))


def simulate():
    FLOORS = take_input_int("Enter number of floors:\n")
    parking_floors = []
    for i in range(0, FLOORS):
        print(f"Press Enter to continue for input of floor: {i}\n")
        park_type_slots_dict = dict()
        for park_type in ParkingSpotType:
            num_spots = int(input(f"Enter how many spots for type: {park_type.name}\n"))
            parking_spots = [ParkingSpot(park_type, i)] * num_spots
            park_type_slots_dict[park_type] = ParkingSpotTypeFloorSpotsMap.get(park_type)(parking_spots)
        parking_floors.append(ParkingFloor(i, park_type_slots_dict, [FloorDisplay()]))
    parking_spot_type = ParkingSpotType(enter_spot_type())
    floor = int(input(f"Enter floor number (any number from 0 to {FLOORS - 1} and -1 if you any will work): \n"))
    free_spot = None
    parkint_ticket_helper = ParkingTicketHelper()
    floors_to_search = parking_floors if floor == -1 else [parking_floors[floor]]
    for fl in floors_to_search:
        try:
            free_spot = fl.find_free_spot(parking_spot_type)
            break
        except NoFreeSpotFoundException as e:
            pass
    if free_spot is not None:
        print(
            f"Parking available at floor:{free_spot.floor} with id: {free_spot._id}\n Parking type :{free_spot.spot_type.name}")
        yes = (input(f"Do you want to take this spot?")).lower() == "y"
        if yes:
            parking_floors[free_spot.floor].occupy_spot(free_spot.spot_type, free_spot._id)
            ticket_id = parkint_ticket_helper.generate_ticket(free_spot)
            print(f"Your ticket is {ticket_id}, Please save it!")
        ticket_id = int(input("Enter your ticket number to release the spot!"))
        if ticket_id is not None:
            ticket = parkint_ticket_helper.release_ticket(ticket_id)
            spot = ticket.spot
            floor_id = spot.floor
            spot_id = spot._id
            spot_type = spot.spot_type
            parking_floors[floor_id].free_spot(ParkingSpotType(spot_type), spot_id)
            cost = ticket.cost
            print(f"Please pay  {cost} rupees!")
    else:
        print("No floor available at the moment, Please try later...")


if __name__ == "__main__":
    # 5 floors
    while 1:
        simulate()
