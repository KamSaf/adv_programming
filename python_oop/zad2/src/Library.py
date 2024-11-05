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
