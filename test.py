import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import pandas as pd
from requests import get
from datetime import time
#from currencies import Currency
# from currencies import Currency (chciałam zamiast tworzenia listy walut ,pobrać ją z biblioteki currencies,ale nie wiem potem jak sprawdzić ,czy otrzymana przez input waluta jest w danej bibliotece

import  json
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


months = mdates.MonthLocator()
days = mdates.DayLocator()
monthsFmt = mdates.DateFormatter('%M')

loader = QUiLoader()
app = QApplication(sys.argv)

window = loader.load("Qt2.ui", None)

window.show()
app.exec()

print ("Kurs walut NBP")

currencies_list=['thb', 'usd', 'aud', 'hkd', 'cad', 'nzd', 'sgd', 'eur','huf', "chf", "gbp", "uah", "jpy", "czk", "dkk", "isk", "nok", "sek", "ron", "bgn", "try", "ils", "clp", "php", "mxn", "zar", "brl"]


while True:
    currency = input("Podaj skrót interesującej Cię waluty: ")
    currency = currency.lower()
    if currency in currencies_list:
        print ("Podany skrót waluty został zlokalizowany w bazie NBP")
        break
    else:
        print("Podany skrót waluty nie został zlokalizowany w bazie NBP, spróbuj jeszcze raz")



start_date = input("od jakiej daty pobrac kurs waluty (RRRR-MM-DD):")

end_date = input("do jakiej daty pobrac kurs waluty (RRRR-MM-DD):")
#if start_date < end_date:
#    print ("data początkowa jest pozniejsza ,niz ")
answer = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{start_date}/{end_date}/?format=json")

dane = answer.json()
print(dane)




kurs = dane['rates']
print (kurs)
df = pd.DataFrame(kurs)
print(df)
df.drop('no', axis=1, inplace=True)
print(df)

df.rename(
    columns=({ 'effectiveDate':'Data', 'mid':'Kurs'}),
    inplace=True,
)
print(df)
x = df['Data']
y = df['Kurs']
df['MA_5'] = df['Kurs'].rolling(5).mean()
df['MA_10'] = df['Kurs'].rolling(20).mean()
df['MA_20'] = df['Kurs'].rolling(50).mean()
#axis[]
plt.figure(figsize=(10,10))
plt.plot(x, y, label='Kurs')
plt.plot(x, df['MA_5'], label='MA_5')
plt.plot(x, df['MA_10'], label='MA_10')
plt.plot(x, df['MA_20'], label='MA_20')
plt.grid(True)

plt.legend(loc=2)
#ax.xaxis.set_major_locator(days)
#ax.xaxis.set_major_formatter(monthsFmt)
#ax.xaxis.set_major_locator(months)

#datemin = datetime.date(x.date.min().month, 1, 1)
#datemax = datetime.date(x.date.max().month + 1, 1, 1)
#ax.set_xlim(datemin, datemax)
plt.xlabel("Czas")
plt.ylabel('Wartość w PLN')
plt.title ("Średni kurs " + currency + " między ( " + start_date + ' a ' + end_date + ' )' )
plt.show()

