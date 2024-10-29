"""
2. Stworzyć następujące klasy:
Library (klasa opisująca bibliotekę), posiadająca pola:
    - city
    - street
    - zip_code
    - open_hours (str)
    - phone
Employee (klasa opisująca pracownika biblioteki), posiadająca pola:
    - first_name
    - last_name
    - hire_date
    - birth_date
    - city
    - street
    - zip_code
    - phone
Book (klasa opisująca książkę), posiadająca pola
    - library
    - publication_date
    - author_name
    - author_surname
    - number_of_pages
Order (klasa opisująca zamówienie), posiadająca pola:
    - employee
    - student
    - books (lista obiektów klasy Book)
    - order_date
Dodatkowo:
Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie
opisywała obiekt oraz ewentualne obiekty znajdujące się w tym obiekcie
(np. obiekt Library w obiekcie Book).
Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
tworzenia instancji klasy za pośrednictwem konstruktora.
Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3
studentów, oraz 2 zamówienia.
Wyświetlić oba zamówienia ( print )
"""

from datetime import datetime
import textwrap
from zad1 import Student


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

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


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: datetime,
        birth_date: datetime,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

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


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: datetime,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        attributes = vars(self)
        output = []
        for key, value in attributes.items():
            if key == "library":
                output.append(f"Library:\n{textwrap.indent(str(value), '  ')}")
            else:
                output.append(f"{key.capitalize().replace('_', ' ')}: {value}")
        return "\n".join(output) + "\n"


class Order:
    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: list[Book],
        order_date: datetime,
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        attributes = vars(self)
        output = []
        for key, value in attributes.items():
            if key == "books":
                for book in value:
                    output.append(f"Books:\n{textwrap.indent(str(book), '  ')}")
            elif key == "employee" or "student":
                output.append(
                    f"{key.capitalize()}:\n{textwrap.indent(str(value), '  ')}"
                )
            else:
                output.append(f"{key.capitalize().replace('_', ' ')}: {value}")
        return "\n".join(output) + "\n"


if __name__ == "__main__":
    libraries = [
        Library(
            city="Warszawa",
            street="ul. Marszałkowska 1",
            zip_code="00-001",
            open_hours="Pon-Pt: 9:00 - 18:00",
            phone="123-456-789",
        ),
        Library(
            city="Kraków",
            street="ul. Floriańska 2",
            zip_code="31-021",
            open_hours="Pon-Pt: 10:00 - 19:00",
            phone="987-654-321",
        ),
    ]

    books = [
        Book(
            library=libraries[0],
            publication_date=datetime(2020, 1, 15),
            author_name="Jan",
            author_surname="Kowalski",
            number_of_pages=300,
        ),
        Book(
            library=libraries[0],
            publication_date=datetime(2019, 5, 23),
            author_name="Anna",
            author_surname="Nowak",
            number_of_pages=250,
        ),
        Book(
            library=libraries[1],
            publication_date=datetime(2021, 3, 10),
            author_name="Piotr",
            author_surname="Zalewski",
            number_of_pages=400,
        ),
        Book(
            library=libraries[1],
            publication_date=datetime(2022, 7, 30),
            author_name="Maria",
            author_surname="Kwiatkowska",
            number_of_pages=150,
        ),
        Book(
            library=libraries[0],
            publication_date=datetime(2018, 8, 5),
            author_name="Jakub",
            author_surname="Wójcik",
            number_of_pages=320,
        ),
    ]

    employees = [
        Employee(
            first_name="Jan",
            last_name="Golec",
            hire_date=datetime(2020, 6, 15),
            birth_date=datetime(1990, 4, 20),
            city="Warszawa",
            street="ul. Marszałkowska 1",
            zip_code="00-001",
            phone="784-472-198",
        ),
        Employee(
            first_name="Wojciech",
            last_name="Gibas",
            hire_date=datetime(2019, 3, 1),
            birth_date=datetime(1985, 7, 10),
            city="Kraków",
            street="ul. Floriańska 2",
            zip_code="31-021",
            phone="627-223-119",
        ),
        Employee(
            first_name="Aleksander",
            last_name="Lewandowski",
            hire_date=datetime(2021, 1, 10),
            birth_date=datetime(1995, 11, 5),
            city="Wrocław",
            street="ul. Oławska 3",
            zip_code="50-123",
            phone="724-982-233",
        ),
    ]

    students = [
        Student(name="Jacek Wilk", marks=[5, 5, 5, 6]),
        Student(name="Jakub Zając", marks=[3, 5, 5, 4]),
        Student(name="Marcin Luter", marks=[5, 4, 4, 2]),
    ]

    orders = [
        Order(
            employee=employees[0],
            student=students[0],
            books=books[0:2],
            order_date=datetime(2024, 10, 28),
        ),
        Order(
            employee=employees[1],
            student=students[1],
            books=books[2:4],
            order_date=datetime(2024, 10, 29),
        ),
    ]

    for index, order in enumerate(orders):
        print(f"Order {index + 1}:")
        print(textwrap.indent(str(order), "  "))
        print("\n\n")
