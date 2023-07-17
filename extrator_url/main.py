url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(f'url completa: {url}')

indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]
print(f'base da url: {url_base}')

url_parametros = url[indice_interrogacao+1:] #x+1 para excluir o separador
print(f'parâmetros da url: {url_parametros}')

#essa abordagem problemas pq a url podem mudar de posição

#encontrar posição de operador na url usando fin()
