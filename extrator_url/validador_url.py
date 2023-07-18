#3 passos para validar usando regex
    #compilar padrão
    #compara com string
    #verificar se retornou combinação (se foi emcontrado)

# https://www.bytebank.com.br/cambio
import re #para importar bibliotecas de regex

url = 'https://www.bytebank.com.br/cambio'
# ()-> define /  {} ->
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError('A url não é válida.')

print("A url é válida.")