import pandas as pd
from requests import get
from datetime import time
# from currencies import Currency (chciałam zamiast tworzenia listy walut ,pobrać ją z biblioteki currencies,ale nie wiem potem jak sprawdzić ,czy otrzymana przez input waluta jest w danej bibliotece
import  json

print ("Kurs walut NBP")

currencies_list=['thb', 'usd', 'aud', 'hkd', 'cad', 'nzd', 'sgd', 'eur','huf']

numerator = 0

currency = input("Podaj skrót interesującej Cię waluty: ")
currency = currency.lower()

if currency in currencies_list:
        print ("Podany skrót waluty został zlokalizowany w bazie NBP")


start_date = input("od jakiej daty pobrac kurs waluty (RRRR-MM-DD):")

end_date = input("do jakiej daty pobrac kurs waluty (RRRR-MM-DD):")
if start_date < end_date:
    print ("data początkowa jest pozniejsza ,niz ")
answer = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{start_date}/{end_date}/?format=json")

dane = answer.json()
print(dane)


