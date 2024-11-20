from .elevator.Elevator import Elevator
from .elevator.ElevatorController import ElevatorController


if __name__ == '__main__':
    elevator_1_id = 1
    elevator_2_id = 2

    n_floor = int(input('Введите количество этажей в доме: '))
    current_floor_1, current_floor_2 = map(int, input('Введите начальные положения лифтов (через пробел): ').split())

    elevators = [
        Elevator(elevator_id=elevator_1_id, current_floor=current_floor_1),
        Elevator(elevator_id=elevator_2_id, current_floor=current_floor_2)
    ]

    controller = ElevatorController(elevators=elevators, n_floor=n_floor)

    flag = True

    # while flag:
        

