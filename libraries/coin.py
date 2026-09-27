import requests

cep = "37701069"
url = f"https://brasilapi.com.br/api/cep/v1/{cep}"

response = requests.get(url)

print(f"Status da resposta: {response.status_code}")

if response.status_code == 200:
    print(response.json())
else:
    print(f"Erro ao consultar o CEP {cep}: {response.status_code}")