import requests

url = "https://www.athexgroup.gr/en/fragments/index-tabs?symbol=gd"

response = requests.get(url)
response.raise_for_status()

data = response.json()

# o JSON vem como dicionário Python
print(data)

# Exemplo: acessar o preço de fechamento
#closing_price = data["movi"][0]["ClosingPrice"]
print(data)
