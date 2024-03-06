import json
import telebot
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

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[base_ticker]



        return total_base


