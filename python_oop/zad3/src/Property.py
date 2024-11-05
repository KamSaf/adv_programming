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
