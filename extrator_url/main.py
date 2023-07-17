url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(f'url completa: {url}')

url_base = url[0:27]
print(f'base da url: {url_base}')

url_parametros = url[28:]
print(f'parêmtros da url: {url_parametros}')

#essa abordagem problemas pq a url podem mudar de posição

#encontrar posição de operador na url
