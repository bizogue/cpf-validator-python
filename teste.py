# validador de cpf
# criação das listas a serem usadas
cpf = []
lista2 = []
nova_lista1 = []
soma2 = soma = 0
resp = 's'
resultado_final = []
verificacao = {}
validos = invalidos = 0
while True:
    # leitura do cpf
    for x in range(0, 11, 1):
        cpf.append(str(input(f'Digite o {x+1}º digito de seu cpf:')).strip())
        # verifica se o usuário digitou uma letra
        while cpf[x].isalpha() is True:
            cpf[x] = input(f'Digite o {x+1}º digito de seu cpf:')
        cpf[x] = int(cpf[x])

    # verificação para a entrada de apenas números positivos até 9
        while cpf[x] < 0 or cpf[x] > 9:
            cpf[x] = int(input(f'Digite o {x+1}º digito de seu cpf:'))

    verificacao['CPF'] = cpf[:]

    # insere os números de 2 até 10 em ordem decrescente em uma lista
    for y in range(10, 1, -1):
        lista2.append(y)
    # PARTE DO 1º DÍGITO
    # faz a multiplicação dos 9 números digitados e os números inseridos na lista2,
    # após isso, faz a soma das multiplicações
    for i in range(0, 9, 1):
        num = cpf[i] * lista2[i]
        soma += num
        # insere a lista1 em uma nova lista para realizar o passo 2, gerar o 11º dígito
        nova_lista1.append(cpf[i])

    # verifica o resto da divisão da soma por 11.
    # se for menor que 2, o 10º dígito será 0,
    if soma % 11 < 2:
        # insere o 10º número junto aos 9 digitados pelo usuário anteriormente
        nova_lista1.append(0)
    else:
        # se não será o resultado da subtração (11 - resto da divisão por 11)
        nova_lista1.append(11 - (soma % 11))
    lista2.insert(0, 11)
    # faz a multiplicação dos 9 números digitados mais o
    # primeiro dígito verificador e os números inseridos na lista2,
    # após isso, faz a soma das multiplicações
    # PARTE DO 2º DÍGITO
    for i in range(0, 10, 1):
        num2 = nova_lista1[i] * lista2[i]
        soma2 += num2
    # verifica o resto da divisão da soma por 11.
    # se for menor que 2, o 11º dígito será 0,
    if soma2 % 11 < 2:
        # insere o 11º número junto aos 9 digitados pelo usuário
        # anteriormente mais o primeiro dígito verificador
        nova_lista1.append(0)
    else:
        # se não será o resultado da subtração (11 - resto da divisão por 11)
        nova_lista1.append(11 - (soma2 % 11))
    if nova_lista1 == cpf:
        verificacao['validacao'] = 'válido'
        validos += 1
        print('CPF válido')
    else:
        print('CPF inválido')
        invalidos += 1
        verificacao['validacao'] = 'inválido'
    resultado_final.append(verificacao.copy())
    cpf.clear()
    nova_lista1.clear()
    resp = input('Deseja continuar verificando CPFs? (Aperte qualquer tecla para parar) ').lower()
    if resp != 's' or resp != 'sim':
        break

    # print apenas para teste
print('=-'*30)
print(f'Total de CPFs testados = {validos + invalidos}')
print(f'Quantidade de CPFs válidos = {validos}')
print(f'Quantidade de CPFs inválidos = {invalidos}')
print(f'Porcentagem de CPFs válidos = {(validos*100)/(validos + invalidos)}%')
print(f'Porcentagem de CPFs válidos = {(invalidos*100)/(validos + invalidos)}%')