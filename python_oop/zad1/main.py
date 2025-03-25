"""
Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
zwracała true , a dla drugiego false .
"""

from src.Student import Student

if __name__ == "__main__":
    students = [Student("John", [5, 5, 5, 6]), Student("James", [3, 5, 5])]
    for s in students:
        print(s)
