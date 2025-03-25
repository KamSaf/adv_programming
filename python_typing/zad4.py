"""
Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
informację jako typ logiczny bool
"""


def check_sum(x: int, y: int, z: int) -> bool:
    return x + y >= z


print(check_sum(2, 2, 3))
