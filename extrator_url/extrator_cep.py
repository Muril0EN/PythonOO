endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ 23440-120'

import re #regular expressions -- RegEx

#cep = 5 digitos + hífen (opcional) + 3 dígitos
                                                                              #opcional
padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')#{}pode receber a-z
busca = padrao.search(endereco) #match ou none
if busca:
    cep=busca.group()
    print(cep)