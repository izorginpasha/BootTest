import json

import requests
from  config import keys

class ConvertionException(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException("Невозможно перевести одинаковые валюты")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не уалось обработать валюту {quote} проверте правильность ввода')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не уалось обработать валюту {base} проверте правильность ввода')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не уалось обработать количество {amount} проверте правильность ввода')

        r = requests.get(f'https://currate.ru/api/?get=rates&pairs={quote_ticker}{base_ticker}&key=e8df781119d3ee4fc2c29a050c24b3a7')
        total_base = float(json.loads(r.content)['data'][quote_ticker+base_ticker])*amount

        return total_base
