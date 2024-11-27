class Elevator:
    def __init__(self, elevator_id: int, current_floor: int) -> None:
        self._elevator_id = elevator_id
        self._current_floor = current_floor

    def get_current_floor(self) -> int:
        return self._current_floor
    
    def up(self) -> None:
        self._current_floor += 1
        print(f'Лифт #{self._elevator_id} поднялся на этаж {self._current_floor}')
        
    def down(self) -> None:
        self._current_floor -= 1
        print(f'Лифт #{self._elevator_id} спустился на этаж {self._current_floor}')
        
    def __open_door(self) -> None:
        print(f'Лифт #{self._elevator_id} открыл дверь')
        
    def __close_door(self) -> None:
        print(f'Лифт #{self._elevator_id} закрыл дверь')
        
    def wait(self) -> None:
        self.__open_door()
        self.__close_door()
