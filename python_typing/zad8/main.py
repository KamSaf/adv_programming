"""
Dla chętnych Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city ,
który może być przekazywany w wierszu poleceń podczas wykonywania (np.
python main.py --city=Berlin ). Należy wykorzystać moduł argparse do
wczytywania przekazywanych parametrów, a w razie przekazania wartości
ograniczyć pobierane browary do miasta, które zostało wskazane.
"""

import argparse
from src.Brewery import Brewery

parser = argparse.ArgumentParser()
parser.add_argument("--city")
args = parser.parse_args()
city = args.city.replace(" ", "_").lower() if args.city else None
breweries = [Brewery(obj) for obj in list(Brewery.fetch_data(count=20, city=city))]

for brewery in breweries:
    print(str(brewery) + "\n")
