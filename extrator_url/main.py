url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"

#separa base e parâmetros
indice_interrogacao = url.find('?') #encontra índice do separador de base/ parâmetros
url_base = url[:indice_interrogacao] #define variável como conteúde de slice que vai do início até índice definido acima

url_parametros = url[indice_interrogacao+1:] #define valor para variável com valor do slice (x+1 para excluir o separador)
print(f'parâmetros da url: {url_parametros}')

#busca o valor de parâmetros
parametro_de_busca = 'quantidade' #define string a ser procurada
indice_parametro = url_parametros.find(parametro_de_busca) #encontra nos parâmetro, pelo índice, o valor a ser buscado
indice_valor = indice_parametro + len(parametro_de_busca) + 1 #soma o tamanho do parâmetro com o índice do parâmetro
#para encontrar o ídice do valor
valor = url_parametros[indice_valor:] #atribui o valor a uma variável através de slice
indice_e_comercial = url_parametros.find('&', indice_valor) #variável que informa poscição de possível separador de parâmetros
if indice_e_comercial == -1: #verfica se há valor de após
    valor = url_parametros[indice_valor:] #faz slice do início da posição do parâmetro procurado até final
else:
    valor = url_parametros[indice_valor: indice_e_comercial] #faz slice até próximo separador e isola o parâmetro

print(f'valor: {valor}')