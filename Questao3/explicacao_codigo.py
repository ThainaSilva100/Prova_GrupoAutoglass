'''
Explique o código abaixo.
01 import requests
02 import json
03 
04 url = 'https://api.github.com/some/endpoint'
05 
06 headers = {‘header’: ‘header1’}
07 payload = {data: 'data1'}
08
09 resp = requests.post(url, data=json.dumps(payload), headers=headers)
10
11 if resp.status_code == 200:
12 resp = json.loads(resp.content)
13 print(resp.content)

'''

'''
## Explicação do código linha a linha:

01 import requests 
--> É feita a importação da biblioteca "requests" que é utilizada para fazer requisições HTTP, enviando e 
recebendo dados de servidor ou API.

02 import json 
--> É feita a importação da biblioteca "json" que permite trabalhar com dados no formato JSON.

04 url = 'https://api.github.com/some/endpoint'
--> Define a URL de uma API ou servidor onde será feita a requisição, nesse caso, é o site do GitHub.

06 headers = {‘header’: ‘header1’} 
--> O "headers" funciona como um cabeçalho onde deve ser passado informações como login ou dados que sejam 
necessários para acessar uma requisição HTTP. E é preciso usar aspas simples.

07 payload = {data: 'data1'} 
--> O "payload" funciona como uma carga que guarda os dados que quero enviar no corpo da requisição HTTP.

09 resp = requests.post(url, data=json.dumps(payload), headers=headers) 
--> Faz uma requisição do tipo POST (envio de dados) para a URL informada. Convertendo o payload para JSON antes 
de enviar e enviando o headers junto com ele, armazenando o retorno da requisição na variável "resp".

11 if resp.status_code == 200: 
--> Se o retorno da variável "resp" for 200, quer dizer que a requisição foi realizada com sucesso.

12 resp = json.loads(resp.content) 
--> Após retornar com sucesso, o "resp.content" onde guarda o conteúdo retornado da requisição, é convertido 
de JSON para um formato que possa ser entendido pelo Python.

13 print(resp.content) 
--> Por fim, é exibido na tela o retorno da requisição HTTP.

Resumindo, o código acima faz uma requisição POST para uma URL na qual é passada informações de cabeçalho (headers)
e dados esperados (payload) que buscam informações e retornam as mesmas em JSON convertendo para a linguagem de 
máquina que o Python possa entender e exibir na tela.

'''