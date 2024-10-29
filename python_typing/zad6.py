"""
Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
powstałą listę.
"""


def process_lists(list_1: list, list_2: list) -> list:
    return [item**3 for item in set(list_1 + list_2)]


print(process_lists([1, 2, 3], [3, 5, 6]))
