from Elevator import Elevator
from ElevatorController import ElevatorController


if __name__ == '__main__':
    n_floor = 9
    current_floor_1, current_floor_2 = 3, 1

    elevators = [
        Elevator(elevator_id=1, current_floor=current_floor_1),
        Elevator(elevator_id=2, current_floor=current_floor_2)
    ]

    controller = ElevatorController(elevators=elevators, n_floor=n_floor)

    controller(8, 0, 1)
