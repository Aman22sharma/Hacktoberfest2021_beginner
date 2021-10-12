#AUTHOR: JoaquinMontesinos
#Python3 Concept: Normalice dates
#GITHUB: https://github.com/JoaquinMontesinos

import datetime
from datetime import datetime
import re
import locale
locale.setlocale(locale.LC_ALL, "")

def clean_date(dates):
    possible_format = ['%d.%m.%y', '%d/%m/%y', '%d/%m/%Y']
    convert_dates = []
    ko = True
    for formats in possible_format:
        try:
            temp = datetime.strptime(dates, formats).strftime('%Y-%m-%d %H:%M:%S')
            convert_dates.append(temp)
            ko = False
            break
        except Exception as e: pass
    if ko:
        convert_dates.append(None)
    dates=convert_dates[0]
    return dates


date=clean_date('03.05.19')
print(date)