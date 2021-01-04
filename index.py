from ModelCliente import Cliente

print('(1)Cadastrar novo cliente | (2)Buscar Cliente | (3)Encerrar programa')
escolha = int(input('Qual ação deseja efetuar:\n'))

while (escolha != 3):

    if (escolha == 1):
        nome = input('Digite o nome do cliente:\n')
        sobrenome = input('Digite o sobrenome do cliente:\n')
        telefone = int(input('Digite o telefone do cliente:\n'))
        endereco = input('Digite o endereco de entrega:\n')
        cliente = Cliente()
        cliente.inclui_cliente(nome,sobrenome,telefone,endereco)

    elif (escolha == 2):
        telefone = input("Digite o telefone do cliente:\n")
        cliente = Cliente()
        cliente.get_info(telefone)

    print('(1)Cadastrar novo cliente | (2)Buscar Cliente | (3)Encerrar programa')
    escolha = int(input('Qual ação deseja efetuar:\n'))

print('************Encerrando sistema! Até logo =)*************')