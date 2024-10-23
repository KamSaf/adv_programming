"""
Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
tekst "Liczba parzysta" / "Liczba nieparzysta"
"""


def is_even(num: int) -> bool:
    return not bool(num % 2)


result = is_even(3)
print("Liczba parzysta") if result else print("Liczba nieparzysta")
