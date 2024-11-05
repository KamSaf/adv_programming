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
