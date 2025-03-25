from datetime import datetime
import textwrap
from src.Library import Library


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
