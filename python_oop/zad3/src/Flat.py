from src.Property import Property


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area=area, rooms=rooms, price=price, address=address)
        self.floor = floor
