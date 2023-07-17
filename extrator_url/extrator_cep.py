endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ 23440-120'

import re #regular expressions -- RegEx

#cep = 5 digitos + hífen (opcional) + 3 dígitos
                                                                              #opcional
padrao = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]')
busca = padrao.search(endereco) #match ou none
if busca:
    cep=busca.group()
    print(cep)