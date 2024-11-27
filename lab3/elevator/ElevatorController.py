import typing as t
from Elevator import Elevator
from ElevatorFSM import ElevatorFSM


class ElevatorController:
    def __init__(self, elevators: list[Elevator], n_floor: int) -> None:
        self._elevators_fsm = list(map(lambda elevator: ElevatorFSM(n_floor, elevator), elevators))
        self._n_floor = n_floor
        
    def __go_to(self, elevator_fsm: ElevatorFSM, start_state: tuple, direction: int, require_floor: int) -> None:
        elevator = elevator_fsm.get_elevator()
        is_final = elevator.get_current_floor() == require_floor
        is_wait = False

        while not (is_final and is_wait):
            action = (direction, is_final)
            start_state, handler = elevator_fsm.next(start_state, action)
            handler()

            is_final = elevator.get_current_floor() == require_floor
            is_wait = start_state[-1] == 2
        
        
    def __call__(self, current_floor: int, direction: int, next_floor: int) -> None:
        nearest_elevator = min(
            self._elevators_fsm, 
            key=lambda elevator_fsm: abs(current_floor - elevator_fsm.get_elevator().get_current_floor())
        )
        
        self.__go_to(
            nearest_elevator, (
                nearest_elevator.get_elevator().get_current_floor(), 2
            ), 
            current_floor - nearest_elevator.get_elevator().get_current_floor() >= 0, 
            current_floor
        )
        
        self.__go_to(
            nearest_elevator, (current_floor, 2), 
            direction, 
            next_floor
        )   
