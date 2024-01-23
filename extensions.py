import requests
import json
from config import keys

class ConvertionExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: float):
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'не удалось обработать количество {amount}.')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base
