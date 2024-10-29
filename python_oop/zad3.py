"""
Stworzyć następujące klasy:
Property (klasa opisująca posiadłość/nieruchomość), posiadająca pola:
    - area
    - rooms (int)
    - price
    - address
House (klasa dziedzicząca klasę Property , która opisuje dom), posiadająca pola:
    - plot (rozmiar działki, int)
Flat (klasa dziedzicząca klasę Property , która opisuje mieszkanie), posiadająca pola:
    - floor

Dodatkowo:
Każda z klas dziedziczących ma mieć zaimplementowaną metodę __str__, która będzie opisywała
obiekt. Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
tworzenia instancji klasy za pośrednictwem konstruktora.
Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je wyświetlić.
"""


class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        attributes = vars(self)
        return (
            "\n".join(
                [
                    f"{key.capitalize().replace('_', ' ')}: {value}"
                    for key, value in attributes.items()
                ]
            )
            + "\n"
        )


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area=area, rooms=rooms, price=price, address=address)
        self.plot = plot


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area=area, rooms=rooms, price=price, address=address)
        self.floor = floor


house = House(
    area=150.0, rooms=5, price=500000.0, address="ul. Słoneczna 10, Warszawa", plot=300
)
flat = Flat(
    area=70.0, rooms=3, price=300000.0, address="ul. Kwiatowa 5, Kraków", floor=2
)

print(house)
print(flat)
