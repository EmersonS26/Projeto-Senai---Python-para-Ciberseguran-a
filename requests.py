#import requests

cep = '04023-001 , 105'

response = requests.get('https://viacep.com.br/ws/{cep}/json/')

print(response.text)