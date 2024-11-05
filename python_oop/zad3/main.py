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

from src.House import House
from src.Flat import Flat


house = House(
    area=150.0, rooms=5, price=500000.0, address="ul. Słoneczna 10, Warszawa", plot=300
)
flat = Flat(
    area=70.0, rooms=3, price=300000.0, address="ul. Kwiatowa 5, Kraków", floor=2
)

print(house)
print(flat)
