"""
Stworzyć skrypt pythonowy, który połączy się z API, które zawiera informacje
o browarach (dokumentacja https://www.openbrewerydb.org/documentation).
Należy w pythonie zrobić klasę
Brewery , która będzie zawierała takie atrybuty jakich dostarcza API wraz z
odpowiednim typowaniem.
W klasie należy zaimplementować magiczną metodę
__str__ która będzie opisywała dane przechowywane w obiekcie.
Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
utworzyć listę 20 instancji klasy
Brewery , którą przeiteruje i wyświetli każdy obiekt z osobna.
"""

import requests
import json


class Brewery:
    def __init__(self, brewery_data: dict):
        obj_fields = [
            "id",
            "name",
            "brewery_type",
            "address_1",
            "address_2",
            "address_3",
            "city",
            "state_province",
            "postal_code",
            "country",
            "longitude",
            "latitude",
            "phone",
            "website_url",
            "state",
            "street",
        ]

        if not all(field in brewery_data for field in obj_fields):
            raise ValueError("Invalid data provided")

        for field in obj_fields:
            value = brewery_data.get(field)
            if field in ["longitude", "latitude"] and value:
                value = float(value)
            setattr(self, field, value)

    def __str__(self):
        attributes = vars(self)
        return "\n".join(
            [f"{key.capitalize()}: {value}" for key, value in attributes.items()]
        )

    @staticmethod
    def fetch_data(count: int = 20) -> list:
        return json.loads(
            requests.get(
                f"https://api.openbrewerydb.org/v1/breweries?per_page={count}"
            ).text
        )


breweries = [Brewery(obj) for obj in list(Brewery.fetch_data(count=20))]

for brewery in breweries:
    print(str(brewery) + "\n")
