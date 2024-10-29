"""
Stworzyć klasę Student , która posiada 2 parametry (name i marks) oraz jedną
metodę is_passed, która zwraca wartość logiczną, pozytywną gdy średnia
ocen jest > 50 w przeciwnym przypadku negatywną. Następnie należy
stworzyć 2 przykładowe obiekty klasy, tak aby dla pierwszego obiektu metoda
zwracała true , a dla drugiego false .
"""


class Student:
    def __init__(self, name: str, marks: list = []):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        # założyłem, że chodziło o średnią 5.0
        return sum(self.marks) / len(self.marks) > 5.0

    def __str__(self):
        return (
            f"Student: {self.name}\nMarks: {self.marks}\nPassed: {self.is_passed()}\n"
        )


if __name__ == "__main__":
    students = [Student("John", [5, 5, 5, 6]), Student("James", [3, 5, 5])]
    for s in students:
        print(s)
