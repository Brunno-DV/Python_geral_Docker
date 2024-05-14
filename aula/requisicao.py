import requests

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
data = response.json()
taxa_dolar = float(data["USDBRL"]["bid"])
print(f'A taxa do dólar está em: R$ {taxa_dolar:.2f}')