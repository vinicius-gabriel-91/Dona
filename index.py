from ModelCliente import Cliente

print('(1)Cadastrar novo cliente | (2)Lista de clientes | (3)Buscar Cliente |\n'
      '(4)Deletar Cliente | (5)Alterar dados do Cliente |(0)Encerrar programa |')
escolha = int(input('Qual ação deseja efetuar:\n'))

while (escolha != 0):

    if (escolha == 1):
        nome = input('Digite o nome do cliente:\n')
        sobrenome = input('Digite o sobrenome do cliente:\n')
        telefone = int(input('Digite o telefone do cliente:\n'))
        endereco = input('Digite o endereco de entrega:\n')
        cliente = Cliente()
        cliente.inclui_cliente(nome,sobrenome,telefone,endereco)
    elif (escolha == 2):
        cliente = Cliente()
        cliente.get_list()
    elif (escolha == 3):
        telefone = input("Digite o telefone do cliente:\n")
        cliente = Cliente()
        cliente.get_info(telefone)
    elif (escolha == 4):
        id = int(input('Digite o ID do cliente a ser DELETADO:\n'))
        cliente = Cliente()
        cliente.deleta_cliente(id)
    elif (escolha == 5):
        id = int(input('Digite o ID do cliente a ser ALTERADO:\n'))
        cliente = Cliente()
        cliente.altera_cliente(id)

    print('(1)Cadastrar novo cliente | (2)Lista de clientes | (3)Buscar Cliente |\n'
          '(4)Deletar Cliente | (5)Alterar dados do Cliente |(0)Encerrar programa')
    escolha = int(input('Qual ação deseja efetuar:\n'))

print('************Encerrando sistema! Até logo =)*************')