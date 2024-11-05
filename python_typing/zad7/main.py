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

from src.Brewery import Brewery

breweries = [Brewery(obj) for obj in list(Brewery.fetch_data(count=20))]

for brewery in breweries:
    print(str(brewery) + "\n")
