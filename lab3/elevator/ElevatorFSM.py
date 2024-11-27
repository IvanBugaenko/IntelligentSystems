import typing as t
from Elevator import Elevator


class ElevatorFSM:
    def __init__(self, n_floor: int, elevator: Elevator) -> None:
        self._fsm = self.__generate_fsm(n_floor)
        self._action_handler = self.__generate_action_handler(n_floor, elevator)
        self._elevator = elevator
        
    def __generate_fsm(self, n_floor) -> t.Dict[tuple, t.Dict[tuple, tuple]]:
        fsm = {
            (1, 2): {
                (1, 0): (2, 1),
            },
            (1, 0): {
                (0, 1): (1, 2)
            },
            (n_floor, 2): {
                (0, 0): (n_floor - 1, 0),
            },
            (n_floor, 1): {
                (1, 1): (n_floor, 2)
            }
        }

        for floor in range(2, n_floor):
            previous_floor = floor - 1
            next_floor = floor + 1
            fsm[(floor, 0)] = {
                (0, 0): (previous_floor, 0),
                (0, 1): (floor, 2),
            }
            fsm[(floor, 2)] = {
                (0, 0): (previous_floor, 0),
                (1, 0): (next_floor, 1),
            }
            fsm[(floor, 1)] = {
                (1, 0): (next_floor, 1),
                (1, 1): (floor, 2),
            }

        return fsm
    
    def __generate_action_handler(self, n_floor: int, elevator: Elevator) -> t.Dict[tuple, t.Dict[tuple, t.Callable]]:
        action_handler = {
            (1, 2): {
                (1, 0): elevator.up,
            },
            (1, 0): {
                (0, 1): elevator.wait
            },
            (n_floor, 2): {
                (0, 0): elevator.down,
            },
            (n_floor, 1): {
                (1, 1): elevator.wait
            }
        }

        for floor in range(2, n_floor):
            action_handler[(floor, 0)] = {
                (0, 0): elevator.down,
                (0, 1): elevator.wait,
            }
            action_handler[(floor, 2)] = {
                (0, 0): elevator.down,
                (1, 0): elevator.up,
            }
            action_handler[(floor, 1)] = {
                (1, 0): elevator.up,
                (1, 1): elevator.wait,
            }

        return action_handler
    
    def get_elevator(self) -> Elevator:
        return self._elevator
    
    def next(self, state: tuple, action: tuple) -> t.Tuple[tuple, t.Callable]:
        try:
            new_state, handler = self._fsm[state][action], self._action_handler[state][action]
            return new_state, handler
        except KeyError as e:
            raise BaseException('Неверно выбран номер этажа')
