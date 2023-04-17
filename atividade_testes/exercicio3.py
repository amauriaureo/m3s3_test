def ler_dimensoes_objeto():
    volume = 0
    lido_sucesso = False

    while not lido_sucesso:
        altura_lida = input('Altura do objeto (em cm): ')
        altura = validar_medida(altura_lida)
        if altura == -1:
            continue

        comprimento_lido = input('Comprimento do objeto (em cm): ')
        comprimento = validar_medida(comprimento_lido)
        if comprimento == -1:
            continue

        largura_lida = input('Largura do objeto (em cm): ')
        largura = validar_medida(largura_lida)
        if largura == -1:
            continue

        volume = altura * comprimento * largura

        if volume > 100000.0 or volume <= 0:
            print('Não aceitamos objetos com dimensões grandes e/ou zeradas')
            print('Entre com as dimensões desejadas novamente')
            continue

        lido_sucesso = True

    preco_volume = calcular_preco_volume(volume)
    print(f'Volume do Objeto (em cm³): {volume}')
    return preco_volume


def calcular_preco_volume(volume):
    valor_volume = 0.0

    if volume < 1000:
        valor_volume = 10.0
    elif volume >= 1000 and volume < 10000:
        valor_volume = 20.0
    elif volume >= 10000 and volume < 30000:
        valor_volume = 30.0
    elif volume >= 30000 and volume < 100000:
        valor_volume = 20.0

    return valor_volume


def validar_medida(medida):
    try:
        medida_validada = int(medida)
    except:
        print('Você digitou alguma dimensão do objeto com valor não numérico')
        print('Entre com as dimensões desejadas novamente')
        return -1

    return medida_validada


def ler_peso_objeto():
    lido_sucesso = False
    peso = 0

    while not lido_sucesso:
        peso_lido = input('Digite o peso do objeto (em Kg): ')
        try:
            peso = float(peso_lido)
            if peso > 30:
                print('Não é aceito objetos tão pesados')
                print('Por favor entre com o peso novamente')
                continue
            lido_sucesso = True
        except:
            print('Você digitou o peso do objeto com um valor não numérico')
            print('Por favor entre com o peso novamente')

    multiplicador_peso = calcular_multiplicador_peso(peso)
    return multiplicador_peso


def calcular_multiplicador_peso(peso):
    multiplicador = 0

    if peso < 0.1:
        multiplicador = 1.0
    elif peso >= 0.1 and peso < 1:
        multiplicador = 1.5
    elif peso >= 1 and peso < 10:
        multiplicador = 2.0
    elif peso >= 10 and peso <= 30:
        multiplicador = 3.0

    return multiplicador


def ler_rota():
    lido_sucesso = False

    while not lido_sucesso:
        print('Selecione a rota: ')
        print('BR - De Brasília para Rio de Janeiro')
        print('BS - De Brasília para São Paulo')
        print('RB - De Rio de Janeiro para Brasília')
        print('RS - De Rio de Janeiro para São Paulo')
        print('SR - De São Paulo para Rio de Janeiro')
        print('SB - De São Paulo para Brasília')

        rota = input('Digite a rota desejada (utilize as siglas): ')
        rota = rota.lower()
        if rota not in ['br', 'bs', 'rb', 'rs', 'sr', 'sb']:
            print('Você digitou uma rota que não existe')
            print('Por favor digite a rota novamente')
            continue

        lido_sucesso = True

    multiplicador_rota = calcular_multiplicador_rota(rota)
    return multiplicador_rota


def calcular_multiplicador_rota(rota):
    multiplicador = 0.0
    if rota in ['rs', 'sr']:
        multiplicador = 1.0
    elif rota in ['bs', 'SB']:
        multiplicador = 1.2
    elif rota in ['br', 'rb']:
        multiplicador = 1.5

    return multiplicador


def calcular_frete(volume, multiplicador_peso, multiplicador_rota):
    total = volume * multiplicador_peso * multiplicador_rota
    return total


if __name__ == '__main__':
    preco_volume = ler_dimensoes_objeto()
    multiplicador_peso = ler_peso_objeto()
    multiplicador_rota = ler_rota()

    total = calcular_frete(preco_volume, multiplicador_peso, multiplicador_rota)

    resultado_final = (
        f'Total a Pagar (R$): {total} '
        f'(dimensões: {preco_volume} * peso: {multiplicador_peso} * '
        f'rota: {multiplicador_rota})'
    )

    print(resultado_final)
pecas = []


def gerar_codigo():
    tamanho_lista = len(pecas)
    if tamanho_lista > 0:
        ultima_peca = pecas[tamanho_lista - 1]
        ultimo_codigo = ultima_peca['codigo']
        return ultimo_codigo + 1

    return 1


def cadastrar_peca():
    codigo = gerar_codigo()
    print(f'\nCódigo da peça: {codigo:03d}')
    nome = input('Por favor entre com o nome da peça: ')
    fabricante = input('Por favor entre com o fabricante da peça: ')
    valor = float(input('Por favor entre com o valor da peça (R$): '))
    peca = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'valor': valor
    }

    pecas.append(peca)
    print('Peça Adicionada!\n')


def imprimir_peca(peca):
    print(f'Código: {peca["codigo"]:03d}')
    print(f'Fabricante: {peca["fabricante"]}')
    print(f'Valor: {peca["valor"]:.2f} R$')


def consultar_pecas():
    finaliza_consulta = False
    while not finaliza_consulta:
        print('Você selecionou a opção para consultar peças')
        print('Escolha a opção desejada:')
        print('1 - Consultar todas as pecas')
        print('2 - Consultar peças por código')
        print('3 - Consultar peças por fabricante')
        print('4 - Retornar')
        opcao_consulta = int(input('Opção: '))
        print()
        if opcao_consulta == 1:
            for peca in pecas:
                imprimir_peca(peca)
                print('-' * 15)
        elif opcao_consulta == 2:
            codigo = int(input('Digite o código da peça: '))
            for peca in pecas:
                if peca['codigo'] == codigo:
                    imprimir_peca(peca)
                    print('-' * 15)
                    break
        elif opcao_consulta == 3:
            fabricante = input('Digite o fabricante da peça: ')
            for peca in pecas:
                if peca['fabricante'] == fabricante:
                    imprimir_peca(peca)
                    print('-' * 15)
        elif opcao_consulta == 4:
            finaliza_consulta = True
            print()
        else:
            print('Opção inválida. Tente novamente')


def remover_peca():
    print('Você selecionou a opção para remover uma peça')
    codigo = int(input('Código da peça a ser removida: '))
    peca_remover = {}
    for peca in pecas:
        if peca['codigo'] == codigo:
            peca_remover = peca
            break

    pecas.remove(peca_remover)
    print('Peça removida com sucesso')


if __name__ == '__main__':
    opcao = 0
    while opcao != 4:
        print('Escolha a opção desejada')
        print('1 - Cadastrar Peças')
        print('2 - Consultar Peças')
        print('3 - Remover Peças')
        print('4 - Sair')
        opcao = int(input('Opção desejada: '))

        if opcao == 1:
            cadastrar_peca()
        elif opcao == 2:
            consultar_pecas()
        elif opcao == 3:
            remover_peca()
        elif opcao > 4 or opcao < 1:
            print('Opção inválida')

    print('Obrigado por usar nossos aplicativos')
