url = "https://bytebank.com/cambio?moedaOrigem=real"

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:] #x+1 para excluir o separador
print(f'parâmetros da url: {url_parametros}')

parametro_de_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_de_busca)
indice_valor = indice_parametro + len(parametro_de_busca) + 1
valor = url_parametros[indice_valor:]

print(f'valor: {valor}')
#essa abordagem problemas pq a url podem mudar de posição

#encontrar posição de operador na url usando fin()
