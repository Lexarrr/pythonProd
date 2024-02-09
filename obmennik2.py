import requests

INVALUTE = input("Введите валюту, которую вы хотитие поменять: ")
OUTVALUTE = input("Введите валюту, на которую вы хотите поменять: ")
INVALUTE_COUNT = float(input("Сколько Вы хотите поменять? : "))
get_str = f'http://172.20.10.13:8008/convert?fv={INVALUTE}&sv={OUTVALUTE}&vcount={INVALUTE_COUNT}'
print(get_str)
OUTVALUTE_COUNT = requests.get(get_str).json()
print(f"Клиенту нужно выдать {OUTVALUTE_COUNT} {OUTVALUTE}")

