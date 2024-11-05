from datetime import datetime
import textwrap
from src.Student import Student
from src.Book import Book
from src.Employee import Employee


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
