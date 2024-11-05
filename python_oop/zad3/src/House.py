from src.Property import Property


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area=area, rooms=rooms, price=price, address=address)
        self.plot = plot
