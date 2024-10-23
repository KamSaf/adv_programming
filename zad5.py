"""
Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
drugim.
"""


def contains(haystack: list, needle: int) -> bool:
    return needle in haystack


print(contains([1, 2, 3, 4], 4))
