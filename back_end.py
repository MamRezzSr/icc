import jdatetime
import requests
from datetime import datetime

def convert_to_persian(date_string):
    date = datetime.strptime(date_string, "%m/%d/%Y")
    timestamp = date.timestamp()
    date = datetime.fromtimestamp(timestamp)
    persian_date = jdatetime.datetime.fromgregorian(date=date)

    return persian_date

currencies = {
    'Euro': 'price_eur',
    'Great British Pound': 'price_gbp',
    'US Dollar': 'price_dollar_rl',
    'Utd. Arab Emir. Dirham': 'price_aed',
    'Norwegian Kroner': 'price_nok',
    'Swedish Krona': 'price_sek',
    'Iraqi Dinar': 'price_iqd',
    'Chinese Yuan Renminbi': 'price_cny',
    'Turkish Lira': 'price_try',
    'Australian Dollar': 'price_aud',
    'Canadian Dollar': 'price_cad'
}

def changeTo(inc ,outc, inv, date):
    persian_date = convert_to_persian(date)

    year = str(persian_date.year)
    month = str(persian_date.month)
    day = str(persian_date.day)

    inc_to_rial = 1
    outc_to_rial = 1

    #print(inc)
    #print(outc)
    #print(persian_date)

    if inc != "Iranian Rial":
        response = requests.get(f'https://www.tgju.org/?act=archive-tool&noview&client=ajax&v=200&name={currencies[inc]}&year={year}&month={month}&day={day}')
        if response.status_code == 200:
            data = response.json()
            inc_to_rial = float(data["price"])
        else:
            logger.info(f'[-] Error on getting inc: {response.status_code}... please check your internet.')

    if outc != "Iranian Rial":
        response = requests.get(f'https://www.tgju.org/?act=archive-tool&noview&client=ajax&v=200&name={currencies[outc]}&year={year}&month={month}&day={day}')
        if response.status_code == 200:
            data = response.json()
            outc_to_rial = float(data["price"])
        else:
            logger.info(f'[-] Error on getting outc: {response.status_code}... please check your internet.')
    
    #print(f"inc to rial: {inc_to_rial} / outc to rial: {outc_to_rial}")
    #print((inc_to_rial/outc_to_rial)*float(inv))

    output = (inc_to_rial/outc_to_rial)*float(inv)

    return output

def roundUp(output):
    if output == int(output):
        out = f"{int(output):,}"
    else:
        out = f"{output:,.2f}"

    return out