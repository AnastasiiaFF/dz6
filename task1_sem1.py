"""
В модуль 
с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

from datetime import datetime as dt
from calendar import isleap
import sys 

def check_date(date: str):
    try:
        t = dt.strptime(date, '%d.%m.%Y')
        _isleap(t.year)
        return True
    except:
        return False

def _isleap(year: int):
    print("Високосный" if isleap(year) else "Не високосный")

if __name__ == "__main__":
    #print(check_date("24.08.1993"))
    data = input('Введите дату в формате DD.MM.YYYY: ')
    if check_date(data):
        print(f'{data} существует')
    else:
        print(f'{data} не существует')